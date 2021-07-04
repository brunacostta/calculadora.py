investiment = float(input("Insira o valor do seu investimento: "))
peoples_original = 30
original_share = 4
click_average = int(100 / 12)
click_share = int(20 / 3)
news_views = 40


def get_total_original(inv, peop):
    return int(inv * peop)


def get_total_share(peop_original, orl_share):
    return int(peop_original * orl_share)


def get_total_clicks(total_clk, clk_ave):
    return int(total_clk / clk_ave)


def get_total_click_share(total_clk, clk_share):
    return int(total_clk / clk_share)


def get_total_peoples_visual(total_share, total_clk_share):
    return int(total_share + total_clk_share)


total_peoples_original = get_total_original(investiment, peoples_original)
total_share = get_total_share(total_peoples_original, original_share)
total_clicks = get_total_clicks(total_share, click_average)
total_click_share = get_total_click_share(total_clicks, click_share)
total_peoples_visual = get_total_peoples_visual(total_share, total_click_share)

visual_social = total_peoples_visual * news_views


print("O seu anúncio original atingirá a quantidade aproximada de: {} pessoas.".format(total_peoples_original))
print("O total aproximado de visualização será de: {}.".format(visual_social))
