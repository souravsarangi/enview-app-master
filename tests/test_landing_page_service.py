from enview_app.landing_page_service import convert_to_fr


def test_convert_to_fr():
    temp_Cs = [-40, 0, 100]
    temp_Fs = [-40, 32, 212]

    for temp_C, temp_F in zip(temp_Cs, temp_Fs):
        assert convert_to_fr(temp_C) == temp_F
