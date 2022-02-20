from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
app.setBackgroundColor(0, 0, 0)
window.title = 'On Callisto | Planetarium'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False
window.editor_ui.enabled = False

flotext = ("images/callisto/floor.jpg")
jupiter = ("../sim1/images/jupiter.png")

floor = flotext

floorcubes = []
for i in range(-35, 35, 2):
    for j in range(-35, 35, 2):
        floorcubes.append(
            Entity(
                model='cube', 
                collider='box', 
                texture=floor,
                color=color.white,
                scale=(2, 2, 2), 
                position=(i, 0, j)
            )
        )
 
class Helmet(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='cube',
            texture=("images/helmet.png"),
            scale_x=1.9
        )
        
helmet = Helmet()

jupiter = Entity(
    model='sphere',
    texture=jupiter,
    scale=14.8744680851,
    position=(-200, 0, 0)
)

sun = Entity(
    model='sphere',
    texture=("images/sun.png"),
    position=(200,50,100),
    scale=0.3577446699203
)

text = Text(
    text="Callisto | -155°C | G=1,236 m/s² | 1'880'000km de Jupiter",
    origin=(0, -18, -10)
)

Audio(sound_file_name='../sounds/music.mp3', autoplay=True, loop=True)

player = FirstPersonController(
    gravity=0.14556574923,
    speed=1.2
)

def update():
    x = player.get_position()
    if x[1] < -2:
        player.position=(0, 1, 0)

print("\033[92m____________________________________________Interstellar Main Theme by Hans Zimmer____________________________________________\033[0m")
print("\033[92m__________________________________________Developed by Gabriel Dovat (www.galtech.ch)____________________________________\033[0m")

app.run()