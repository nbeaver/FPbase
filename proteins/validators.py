from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# from django.utils.translation import gettext as _
import ast
import re

from Bio import Alphabet, Seq, Data
from .fields import Spectrum
from fpseq.mutations import Mutation

validate_doi = RegexValidator(
    r"^10.\d{4,9}/[-._;()/:a-zA-Z0-9]+$", "Not a valid DOI string"
)
validate_uniprot = RegexValidator(
    r"[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2}",
    "Not a valid UniProt Accession",
)


def validate_mutationset(mutset):
    errors = []
    for mut in re.split(" |,|/|\\\\", mutset):
        if mut:
            try:
                validate_mutation(mut)
            except ValidationError as e:
                errors.append(
                    ValidationError("Bad Mutation String: {}".format(e), code="badmut")
                )
    if errors:
        raise ValidationError(errors)


def validate_mutation(code):
    try:
        code = code.strip()
        m = Mutation.from_str(code)
        if str(m) != code:
            raise ValueError(
                "Parsed mutation ({}) different than input ({})".format(m, code)
            )
    except ValueError as e:
        raise ValidationError("Invalid mutation: %s" % e)


def cdna_sequence_validator(seq):
    badletters = []
    for letter in seq:
        if letter not in Alphabet.IUPAC.unambiguous_dna.letters:
            badletters.append(letter)
    if len(badletters):
        raise ValidationError(
            "Invalid DNA letters: {}".format("".join(set(badletters)))
        )
    try:
        Seq.Seq(seq, Alphabet.IUPAC.unambiguous_dna).translate()
    except Data.CodonTable.TranslationError as e:
        raise ValidationError(e)


def protein_sequence_validator(seq):
    seq = "".join(str(seq).split()).upper()  # remove whitespace
    badletters = []
    for letter in seq:
        if letter not in Alphabet.IUPAC.protein.letters:
            badletters.append(letter)
    if len(badletters):
        badletters = set(badletters)
        raise ValidationError(
            "Invalid letter(s) found in amino acid sequence: {}".format(
                "".join(badletters)
            )
        )


def validate_spectrum(value):
    if not value:
        return None
    if isinstance(value, Spectrum):
        return
    try:
        obj = ast.literal_eval(value)
    except Exception:
        raise ValidationError("Invalid input for a Spectrum instance")
    if not isinstance(obj, list):  # must be a list
        raise ValidationError("Spectrum object must be of type List")
    if not all(
        isinstance(elem, (list, tuple)) for elem in obj
    ):  # must be list of lists
        raise ValidationError("Spectrum object must be a list of lists or tuples")
    for elem in obj:
        if not len(elem) == 2:
            raise ValidationError("All elements in Spectrum list must have two items")
        if not all(isinstance(n, (int, float)) for n in elem):
            raise ValidationError("All items in Spectrum list elements must be numbers")
