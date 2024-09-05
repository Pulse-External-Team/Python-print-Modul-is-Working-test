import pygame
import random
import time
import pygame_gui
from pygame.locals import *

# Pygame Initialisierung
pygame.init()

# Bildschirmgröße
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Komplexer Sortieralgorithmus-Visualizer")

# Farben
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Sound Setup
pygame.mixer.init()

# GUI Setup
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))

# Hinzufügen von Buttons für die GUI
sort_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 50), (120, 50)),
                                           text='Sortieren',
                                           manager=manager)
speed_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((850, 150), (120, 50)),
                                                      start_value=0.01,
                                                      value_range=(0.01, 0.5),
                                                      manager=manager)
reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((850, 250), (120, 50)),
                                            text='Zurücksetzen',
                                            manager=manager)

# Verschiedene Sortieralgorithmen
algorithms = ["Bubble Sort", "Insertion Sort", "Merge Sort", "Quick Sort", "Selection Sort"]
algorithm_dropdown = pygame_gui.elements.UIDropDownMenu(relative_rect=pygame.Rect((850, 350), (120, 50)),
                                                        options_list=algorithms,
                                                        starting_option=algorithms[0],
                                                        manager=manager)

# Startbedingung für Sound und Geschwindigkeit
sort_speed = 0.01

# Zeichne das Array
def draw_array(array, color_array):
    screen.fill(BLACK)
    bar_width = SCREEN_WIDTH // len(array)
    for i in range(len(array)):
        pygame.draw.rect(screen, color_array[i], (i * bar_width, SCREEN_HEIGHT - array[i], bar_width, array[i]))
    pygame.display.update()

# Toneffekt erzeugen (Tonhöhe abhängig von Array-Wert)
def play_sound(value):
    frequency = 200 + (value * 3)
    duration = 50  # Millisekunden
    sound = pygame.mixer.Sound(frequency=frequency, size=-16, channels=1, buffer=512)
    sound.play()
    pygame.time.delay(duration)

# Sortier-Algorithmen

# Bubble Sort
def bubble_sort(array, draw_function, speed):
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
            draw_function(array, [BLUE if x == j or x == j + 1 else WHITE for x in range(len(array))])
            play_sound(array[j])
            time.sleep(speed)

# Insertion Sort
def insertion_sort(array, draw_function, speed):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
        draw_function(array, [GREEN if x == j or x == i else WHITE for x in range(len(array))])
        play_sound(array[i])
        time.sleep(speed)

# Quick Sort
def quick_sort(array, low, high, draw_function, speed):
    if low < high:
        pi = partition(array, low, high, draw_function, speed)
        quick_sort(array, low, pi - 1, draw_function, speed)
        quick_sort(array, pi + 1, high, draw_function, speed)

def partition(array, low, high, draw_function, speed):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
        draw_function(array, [YELLOW if x == i or x == j else WHITE for x in range(len(array))])
        play_sound(array[j])
        time.sleep(speed)
    array[i + 1], array[high] = array[high], array[i + 1]
    draw_function(array, [RED if x == high or x == i + 1 else WHITE for x in range(len(array))])
    return i + 1

# Reset-Array (Zufällige Neuordnung)
def reset_array(array, draw_function):
    random.shuffle(array)
    draw_function(array, [WHITE for _ in array])

# Hauptspiel-Schleife
def game_loop():
    global sort_speed
    num_elements = 100
    array = [random.randint(50, SCREEN_HEIGHT - 50) for _ in range(num_elements)]
    draw_array(array, [WHITE] * len(array))

    sorting = False
    algorithm_selected = None

    while True:
        time_delta = manager.get_delta()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # GUI-Ereignisverarbeitung
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == sort_button:
                        sorting = True
                        algorithm_selected = algorithm_dropdown.selected_option
                    elif event.ui_element == reset_button:
                        reset_array(array, draw_array)
                        sorting = False

                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    sort_speed = event.value

            manager.process_events(event)

        manager.update(time_delta)

        # Sortieralgorithmen ausführen, falls aktiviert
        if sorting:
            if algorithm_selected == "Bubble Sort":
                bubble_sort(array, draw_array, sort_speed)
            elif algorithm_selected == "Insertion Sort":
                insertion_sort(array, draw_array, sort_speed)
            elif algorithm_selected == "Quick Sort":
                quick_sort(array, 0, len(array) - 1, draw_array, sort_speed)
            sorting = False

        manager.draw_ui(screen)
        pygame.display.update()

if __name__ == "__main__":
    game_loop()
