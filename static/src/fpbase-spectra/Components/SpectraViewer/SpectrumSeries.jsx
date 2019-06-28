import React, { memo, useEffect, useState, useRef } from "react"
import { Series } from "react-jsx-highcharts"
import { useApolloClient } from "react-apollo-hooks"
import { GET_SPECTRUM } from "../../client/queries"
import { List } from "immutable"

const OD = num => (num <= 0 ? 10 : -Math.log10(num))

const hex2rgba = (hex, alpha = 1) => {
  const [r, g, b] = hex.match(/\w\w/g).map(x => parseInt(x, 16))
  return `rgba(${r},${g},${b},${alpha})`
}

const CROSS_HATCH = {
  pattern: {
    path: {
      d: ["M 5,5 L 10,10", "M 5,5 L 0,10", "M 5,5 L 10,0", "M 5,5 L 0,0"]
    },
    width: 10,
    height: 10,
    color: "#ddd",
    opacity: 0.4
  }
}

const VERT_LINES = {
  pattern: {
    path: {
      d: ["M 2,10 L 2,0"]
    },
    width: 3,
    height: 10,
    opacity: 0.2
  }
}

class ErrorBoundary extends React.Component {
  // constructor(props) {
  //   super(props)
  //   this.state = { hasError: false }
  // }

  // static getDerivedStateFromError(error) {
  //   // Update state so the next render will show the fallback UI.
  //   return { hasError: true }
  // }

  componentDidCatch(error, info) {
    // You can also log the error to an error reporting service
    // logErrorToMyService(error, info);
  }

  render() {
    // if (this.state.hasError) {
    //   // You can render any custom fallback UI
    //   return this.props.children
    // }

    return this.props.children
  }
}

const useExNormedData = ({ exNorm, spectrum, ownerInfo }) => {
  const client = useApolloClient()
  const [serie, setSerie] = useState(List([...spectrum.data]))

  useEffect(() => {
    async function getExData() {
      if (spectrum.owner.slug in ownerInfo) {
        let scalar = 0
        const ownerSpectra = ownerInfo[spectrum.owner.slug].spectra
        if (ownerSpectra) {
          const exSpectrum =
            ownerSpectra.find(i => i.subtype === "EX") ||
            ownerSpectra.find(i => i.subtype === "AB")
          if (exSpectrum) {
            const {
              data: {
                spectrum: { data: exData }
              }
            } = await client.query({
              query: GET_SPECTRUM,
              variables: { id: exSpectrum.id }
            })
            const exEfficiency = exData.find(([x]) => x === exNorm)
            if (exEfficiency) {
              scalar = exEfficiency[1]
            }
          } else {
          }
        }
        setSerie(List([...spectrum.data].map(([a, b]) => [a, b * scalar])))
      }
    }

    if (spectrum.subtype === "EM" && exNorm) {
      getExData()
    } else {
      setSerie(List([...spectrum.data]))
    }
  }, [
    client,
    exNorm,
    ownerInfo,
    spectrum.data,
    spectrum.owner.slug,
    spectrum.subtype
  ])

  return serie
}

const SpectrumSeries = memo(function SpectrumSeries({
  inverted,
  logScale,
  scaleEC,
  scaleQY,
  spectrum,
  areaFill,
  exNorm,
  ownerInfo
}) {
  let serie = useExNormedData({ exNorm, spectrum, ownerInfo })
  if (!spectrum) return
  const willScaleEC = Boolean(
    spectrum.subtype === "EX" && scaleEC && spectrum.owner.extCoeff
  )
  const willScaleQY = Boolean(
    spectrum.subtype === "EM" && scaleQY && spectrum.owner.qy
  )
  if (willScaleEC) {
    serie = serie.map(([a, b]) => [a, b * spectrum.owner.extCoeff])
  }
  if (willScaleQY) {
    serie = serie.map(([a, b]) => [a, b * spectrum.owner.qy])
  }
  if (inverted) {
    serie = serie.map(([a, b]) => [a, 1 - b])
  }
  if (logScale) {
    serie = [...serie].map(([a, b]) => [a, OD(b)])
  }

  let name = `${spectrum.owner.name}`
  if (["EX", "EM", "A_2P", "2P"].includes(spectrum.subtype)) {
    name += ` ${spectrum.subtype.replace("A_", "")}`
  }
  let color = hex2rgba(spectrum.color, 0.9)
  let fillColor = hex2rgba(spectrum.color, 0.5)
  let lineWidth = 0.5
  let type = areaFill ? "areaspline" : "spline"
  if (spectrum.category === "C") {
    fillColor = CROSS_HATCH
  }
  if (spectrum.category === "L") {
    fillColor = { ...VERT_LINES }
    lineWidth = 1
  }
  if (["BS", "LP"].includes(spectrum.subtype)) {
    lineWidth = 1.5
    type = "spline"
    color = "#999"
  }

  return (
    <ErrorBoundary>
      <Series
        type={type}
        subtype={spectrum.subtype}
        scaleEC={willScaleEC}
        scaleQY={willScaleQY}
        name={name}
        color={color}
        fillColor={fillColor}
        lineWidth={lineWidth}
        className={`cat-${spectrum.category} subtype-${spectrum.subtype}`}
        data={serie}
        threshold={logScale ? 10 : 0}
      />
    </ErrorBoundary>
  )
})

export default SpectrumSeries