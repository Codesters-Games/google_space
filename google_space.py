# change the background
stage.set_background("space4")
# Title: google_8d7
# License: 
# Source: https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0619f23e-580a-4525-ba3b-5d292c9df6b3/dfxokn1-724ade30-23c3-48e8-acd5-5b5da77b09cb.png/v1/fill/w_1280,h_433/google_2015_g_o_o_g_l_and_e_by_toe_may_toe_2_dfxokn1-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NDMzIiwicGF0aCI6IlwvZlwvMDYxOWYyM2UtNTgwYS00NTI1LWJhM2ItNWQyOTJjOWRmNmIzXC9kZnhva24xLTcyNGFkZTMwLTIzYzMtNDhlOC1hY2Q1LTViNWRhNzdiMDljYi5wbmciLCJ3aWR0aCI6Ijw9MTI4MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.UZF227-poE03MUmoCZhMNdmBBaKZioTRXc227K7ChM0
google_logo = codesters.Sprite("google_8d7", 0, 50)
google_logo.set_size(0.6)
# sprite = codesters.Rectangle(x, y, width, height, "color")
search_bar = codesters.Rectangle(0, 0, 250, 16, "white")
search_bar.set_outline_color("red")
# create buttons
search_button = codesters.Rectangle(-80, -60, 1, 1, "white")
lucky_button = codesters.Rectangle(80, -60, 1, 1, "white")

# enable gravity and physics
stage.set_gravity(1.5)
stage.enable_physics()

google_logo.set_x_speed(0.6)
google_logo.set_y_speed(0.9)
google_logo.set_drag_on()
google_logo.set_physics_on()
google_logo.collision_on()

search_bar.set_x_speed(0.6)
search_bar.set_y_speed(0.9)
search_bar.set_drag_on()
search_bar.set_physics_on()
search_bar.collision_on()

search_button.set_x_speed(0.6)
search_button.set_y_speed(0.9)
search_button.set_drag_on()
search_button.set_physics_on()
search_button.collision_on()

lucky_button.set_x_speed(0.6)
lucky_button.set_y_speed(0.9)
lucky_button.set_drag_on()
lucky_button.set_physics_on()
lucky_button.collision_on()


search_button.say("Google Search")
lucky_button.say("I'm Feeling Lucky")

search_button.set_say_background("LightGray", 0.75)
search_button.set_say_color("Black")
lucky_button.set_say_background("LightGray", 0.75)
lucky_button.set_say_color("Black")

while True:
    google_logo.rotate_origin(0.3)
    search_bar.rotate_origin(0.3)
    search_button.rotate_origin(0.3)
    lucky_button.rotate_origin(0.3)




# # create and locate the letters
# first_g_letter = codesters.Text("G", -78, 0, "blue")
# first_o_letter = codesters.Text("o", -50, 0, "red")
# second_o_letter = codesters.Text("o", -26, 0, "gold")
# second_g_letter = codesters.Text("g", 0, 0, "blue")
# l_letter = codesters.Text("l", 19, 0, "green")
# e_letter = codesters.Text("e", 38, 0, "red")

# # make the size bigger for all letter
# first_g_letter.set_text_size(45)
# first_o_letter.set_text_size(45)
# second_o_letter.set_text_size(45)
# second_g_letter.set_text_size(45)
# l_letter.set_text_size(45)
# e_letter.set_text_size(45)

# # change the font to sans for all letter
# first_g_letter.set_text_font("sans")
# first_o_letter.set_text_font("sans")
# second_o_letter.set_text_font("sans")
# second_g_letter.set_text_font("sans")
# l_letter.set_text_font("sans")
# e_letter.set_text_font("sans")

# stage.enable_physics()

# first_g_letter.set_physics_on()
# first_g_letter.set_gravity_on()
# first_o_letter.set_physics_on()
# first_o_letter.set_gravity_on()
# second_o_letter.set_physics_on()
# second_o_letter.set_gravity_on()
# second_g_letter.set_physics_on()
# second_g_letter.set_gravity_on()
# l_letter.set_physics_on()
# l_letter.set_gravity_on()
# e_letter.set_physics_on()
# e_letter.set_gravity_on()

# while True:
#     first_g_letter.rotate_origin(0.5)
#     first_o_letter.rotate_origin(0.5)
#     second_o_letter.rotate_origin(0.5)
#     second_g_letter.rotate_origin(0.5)
#     l_letter.rotate_origin(0.5)
#     e_letter.rotate_origin(0.5)



