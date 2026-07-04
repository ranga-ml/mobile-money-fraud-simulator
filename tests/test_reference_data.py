from src.common.reference_data import ReferenceData


def test_reference_data_loads():

    occupations = ReferenceData.get("occupations")

    assert len(occupations) > 0

    assert "Engineer" in occupations