ploshad_v_sotkah = float(input())
ploshad_v_metrah = ploshad_v_sotkah * 100
dlina_gryadki = 25
shirina_gryadki = 15
ploshad_gryadki = dlina_gryadki * shirina_gryadki
gryadok_na_ychastke = int(ploshad_v_metrah / ploshad_gryadki)
svobodnaya_ploshad = (ploshad_v_metrah - ploshad_gryadki * gryadok_na_ychastke)
print(int(svobodnaya_ploshad))