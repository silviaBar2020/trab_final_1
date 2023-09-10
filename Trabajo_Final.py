
from guizero import App, Drawing, Combo, Slider, Text, PushButton, Picture,TextBox, Window,yesno, error,info

def nombre():
    welcome_message.value = my_name.value
    my_name.show()

def tamaño_de_texto(slider_value):
    welcome_message.size = slider_value

app = App(title="Mi Programa")

welcome_message = Text(app, text="Bienvenido a los datos de su perfil", size=20, font="Times New Roman", color="lightblue")
text_size = Slider(app, command=tamaño_de_texto, start=10, end=80)
text_box = TextBox(app)

update_text = PushButton(app, command=nombre, text="Escriba su nombre")


mi_foto = Picture(app, image="foto.png",width=400,height=400)

window = Window(app, title="Vamos a dibujar")

# Widgets en la segunda ventana
#text = Text(window, text="Este texto se mostrará en la ventana #2")



def start(event):
    painting.last_event = event
    painting.first_event = event
    painting.last_shape = None
    
def draw(event):
    if shape.value == "line":
        painting.line(
            painting.last_event.x, painting.last_event.y,
            event.x, event.y,
            color=color.value,
            width=width.value
        )
    
    if shape.value == "rectangle":
        
        if painting.last_shape is not None:
            painting.delete(painting.last_shape)
        
        rectangle = painting.rectangle(
            painting.first_event.x, painting.first_event.y, 
            event.x, event.y, 
            color=color.value
        )

        painting.last_shape = rectangle
    if shape.value == "oval":
            
            painting.last_shape = painting.oval(
                painting.first_event.x, painting.first_event.y, 
                event.x, event.y, 
                color=color.value
            )

    painting.last_event = event




#window = Window(window, title="Paint")
color = Combo(window, options=["black", "white", "red", "green", "blue","yellow","grey"])
width = Slider(window, start=1, end=10)
shape = Combo(window, options=["line", "rectangle","oval"])

painting = Drawing(window, width="fill", height="fill")

painting.when_left_button_pressed = start
painting.when_mouse_dragged = draw
#app = App(title="Uso de Yes No Box")
build_a_snowman = yesno("Una pregunta", "¿Quiere  dibujar?, si quiere dibujar escriba su nombre")

if build_a_snowman == True:
    info("Snowman", "Perfecto...")
else:
    error("Snowman", "Adios...")
def do_this_on_close():
 # Pregunta al usuario si realmente quiere cerrar la ventana
    if app.yesno("Cerrar", "¿Está seguro de querer salir?"):
        app.destroy()


# Cuando se intenta cerrar la ventana, se ejecuta do_this_on_close()
app.when_closed = do_this_on_close


app.display()
