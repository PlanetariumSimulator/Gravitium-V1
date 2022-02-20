from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
app.setBackgroundColor(0, 0, 0)
window.title = 'On the Moon | Planetarium'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False
window.editor_ui.enabled = False

flotext = ("images/moon/floor.jpg")
earth = ("../sim1/images/earth.png")

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

earth = Entity(
    model='sphere',
    texture=earth,
    scale=12.5,
    position=(-200, 0, 0)
)

text = Text(
    text="Lune | +120°C | G=1,62 m/s² | 384'400km de la Terre",
    origin=(0, -18, -10)
)

Audio(sound_file_name='../sounds/music.mp3', autoplay=True, loop=True)

player = FirstPersonController(
    gravity=0.1651376146788,
    speed=0.8587155963302
)

sun = Entity(
    model='sphere',
    texture=("images/sun.png"),
    position=(200,50,-100),
    scale=1.8569333333333333
)

def update():
    x = player.get_position()
    if x[1] < -2:
        player.position=(0, 1, 0)

print("\033[92m____________________________________________Interstellar Main Theme by Hans Zimmer____________________________________________\033[0m")
print("\033[92m__________________________________________Developed by Gabriel Dovat (www.galtech.ch)____________________________________\033[0m")

app.run()