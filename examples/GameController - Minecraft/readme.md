# GameController - Minecraft Version

Dieser Code ist für ein Minecraft-Makro-Keyboard: Du drückst eine Taste und es schickt ein Kommando los, also zum Beispiel um den Gamemode zu wechseln:

`/gamemode 1`

Es wird zusätzlich nach dem "/" für den Kommando-Modus kurz gewartet.

Zum Anpassen der einzelnen Kommandos einfach diesen Teil hier anpassen:

```python
# Hier sind die einzelnen PINS (Tasten)  definiert und die dazu gehörigen Befehle
buttons = {
    board.GP15: "gamemode 1\n",
    board.GP14: "gamemode 2\n",
    board.GP13: "gamemode 3\n",
    board.GP12: "gamemode 4\n",
}
```