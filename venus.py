from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
app.setBackgroundColor(0, 0, 0)
window.title = 'On Venus | Planetarium'
window.borderless = False
window.fullscreen = True
window.exit_button.visible = False
window.fps_counter.enabled = False
window.editor_ui.enabled = False

flotext = ("images/venus/floor.jpg")
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

class Sky(Entity):
  def __init__(self):
    super().__init__(
      parent=scene,
      model='sphere',
      texture=("images/venus/sky.jpg"),
      scale=500,
      double_sided=True
    )

sky = Sky()
        
helmet = Helmet()

text = Text(
    text="Vénus | +462°C | G=8,87 m/s² | 108'000'000km du Soleil",
    origin=(0, -18, -10)
)

Audio(sound_file_name='../sounds/music.mp3', autoplay=True, loop=True)

player = FirstPersonController(
  gravity=0.90417940876,
  speed=2.6
)

def update():
    x = player.get_position()
    if x[1] < -2:
        player.position=(0, 1, 0)

sun = Entity(
    model='sphere',
    texture=("images/sun.png"),
    position=(-200,50,100),
    scale=2.5741165163389
)

print("\033[92m____________________________________________Interstellar Main Theme by Hans Zimmer____________________________________________\033[0m")
print("\033[92m__________________________________________Developed by Gabriel Dovat (www.galtech.ch)____________________________________\033[0m")
    
app.run()