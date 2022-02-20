from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
app.setBackgroundColor(0, 0, 0)
window.title = 'On the Eart | Planetarium'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False
window.editor_ui.enabled = False

floorcubes = []
for i in range(-35, 35, 2):
    for j in range(-35, 35, 2):
        floorcubes.append(
            Entity(
                model='cube', 
                collider='box', 
                texture='grass',
                color=color.white,
                scale=(2, 2, 2), 
                position=(i, 0, j)
            )
        )

text = Text(
    text="Terre | +15°C | G=9,81 m/s² | 150'000'000km du Soleil",
    origin=(0, -18, -10)
)

Audio(sound_file_name='../sounds/music.mp3', autoplay=True, loop=True)

player = FirstPersonController()

sky=Sky()

sun = Entity(
    model='sphere',
    texture=("images/sun.png"),
    position=(-200,50,100),
    scale=1.8569333333333333
)

def update():
    x = player.get_position()
    if x[1] < -2:
        player.position=(0, 1, 0)

print("\033[92m____________________________________________Interstellar Main Theme by Hans Zimmer____________________________________________\033[0m")
print("\033[92m__________________________________________Developed by Gabriel Dovat (www.galtech.ch)____________________________________\033[0m")
    
app.run()