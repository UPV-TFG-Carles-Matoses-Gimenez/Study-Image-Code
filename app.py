print("importing libraries")
import time
import dearpygui.dearpygui as dpg


print("creating context")
dpg.create_context()
print("context created")

from modules import NODE_WINDOW, NODE_WINDOW_MENU, INSPECTOR_WINDOW
from modules import interaction


# PANTALLA Node
with dpg.window(label="NodeWindow", tag=NODE_WINDOW, width=1920-300, height=1080, max_size=[1920,1080],pos=(300,0)):
    with dpg.menu_bar(tag=NODE_WINDOW_MENU):
        pass
    pass

with dpg.node_editor(callback=interaction.link_callback, delink_callback=interaction.delink_callback, minimap=True, parent=NODE_WINDOW, tag="node editor",):
    pass


from modules import *

# PANTALLA inspector
with dpg.window(label=INSPECTOR_WINDOW,tag=INSPECTOR_WINDOW, width=300, height=1080, max_size=[400,1080],pos=(0,0),):
    pass

COOLDOWN = True
# COMANDOS Y SHORTCUTS
with dpg.handler_registry():
    dpg.add_key_press_handler(dpg.mvKey_Control, callback=interaction.on_key_la)
    dpg.add_key_press_handler(dpg.mvKey_Control, callback=interaction.on_key_la2)

    dpg.add_key_release_handler(dpg.mvKey_X, callback=interaction.on_key_X)
    dpg.add_key_release_handler(dpg.mvKey_D, callback=interaction.on_key_D)


# PANTALLA PADRE
# Funciones
def add_panel(sender, app_data, user_data):
    print(user_data)
    dpg.show_item(user_data)

from modules import WINDOW_SIZE
w = int(WINDOW_SIZE[0]-WINDOW_SIZE[0]*.25)
h = int(WINDOW_SIZE[1]-WINDOW_SIZE[1]*.25)
dpg.create_viewport(title='Study Image', width=w, height=h)

with dpg.viewport_menu_bar():
    # REGISTRO DE PANELES
    with dpg.menu(label="Paneles"):
        dpg.add_menu_item(label=NODE_WINDOW, user_data=NODE_WINDOW, callback=add_panel)
        dpg.add_menu_item(label=INSPECTOR_WINDOW, user_data=INSPECTOR_WINDOW, callback=add_panel)

    dpg.add_menu_item(label="Help", callback=None)

# cool_time = 0
# current_time = time.time()
# last_frame_time = 0
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
# while dpg.is_dearpygui_running():
#     current_time = time.time()
#     if not COOLDOWN:
#         if cool_time >.5:
#             interaction.COOLDOWN = True
#             cool_time = 0
#             print("refresh cooldown")
#         else:
#             cool_time += last_frame_time
#     last_frame_time = time.time()-current_time
#     print(cool_time)
    
#     # insert here any code you would like to run in the render loop
#     # you can manually stop by using stop_dearpygui()
#     dpg.render_dearpygui_frame()

dpg.destroy_context()

