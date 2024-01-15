
# Bilder in SW Konvertieren mit Python

Diese Python-Skript verwendet die PIL (Python Imaging Library) Bibliothek, um Bilder in Schwarzweiss umzuwandeln und dabei Kontrast und Helligkeit anzupassen. Hier ist eine kurze Anleitung zur Verwendung des Skripts:

Installiere PIL: Stelle sicher, dass die PIL-Bibliothek installiert ist. Du kannst sie mit dem folgenden Befehl installieren:

```
pip install pillow
```

Führe das Skript aus: Verwende die Kommandozeile, um das Skript auszuführen. Hier ist ein Beispiel:

## Ein einzelnes Bild konvertieren:

```
    python tci_sw_converter.py -i input_image.jpg -o output_image.jpg -c 1.5 -b 0.8

        -i oder --input: Pfad zum Eingabebild (JPG).
        -o oder --output: Optionaler Pfad zum Ausgabebild (JPG). Wenn nicht angegeben, wird ein Standardname im selben Verzeichnis erstellt.
        -c oder --contrast: Kontrastfaktor (Standard: 1.0).
        -b oder --brightness: Helligkeitsfaktor (Standard: 1.0).
```
 
## Mehrere Bilder im Verzeichnis konvertieren:

    Installiere PIL: Falls noch nicht installiert (wie oben beschrieben).

    Führe das Skript aus: Verwende die Kommandozeile, um das Skript für ein Verzeichnis mit Bildern auszuführen. Hier ist ein Beispiel:

```
    python tci_sw_converter.py -d input_directory -c 1.5 -b 0.8

        -d oder --directory: Pfad zum Verzeichnis mit Bildern für die Stapelverarbeitung.
        -o oder --output: Optionaler Pfad zum Ausgabeverzeichnis. Wenn nicht angegeben, wird ein Ordner mit dem Namen "converted_images" im Eingabeverzeichnis erstellt.
        -c oder --contrast: Kontrastfaktor (Standard: 1.0).
        -b oder --brightness: Helligkeitsfaktor (Standard: 1.0).
```
Hinweis:

Stelle sicher, dass das Skript im gleichen Verzeichnis wie die Bilder oder im Systempfad liegt, damit es ohne Pfadangabe ausgeführt werden kann.


------

This Python script uses the PIL (Python Imaging Library) library to convert images to black and white while adjusting contrast and brightness. Here is a brief guide on how to use the script:


Install PIL: Make sure the PIL library is installed. You can install it using the following command:

```
pip install pillow
```

## Convert a Single Image:

Run the Script: Use the command line to execute the script. Here is an example:


```
    python tci_sw_converter.py -i input_image.jpg -o output_image.jpg -c 1.5 -b 0.8

        -i or --input: Path to the input image file (JPG).
        -o or --output: Optional path to the output image file (JPG). If not specified, a default name will be created in the same directory.
        -c or --contrast: Contrast factor (default: 1.0).
        -b or --brightness: Brightness factor (default: 1.0).
```
## Convert Multiple Images in a Directory:

    Install PIL: If not installed yet (as mentioned above).

    Run the Script: Use the command line to execute the script for a directory with images. Here is an example:

```
    python tci_sw_converter.py -d input_directory -c 1.5 -b 0.8

        -d or --directory: Path to the directory containing images for batch processing.
        -o or --output: Optional path to the output directory. If not specified, a folder named "converted_images" will be created in the input directory.
        -c or --contrast: Contrast factor (default: 1.0).
        -b or --brightness: Brightness factor (default: 1.0).
```

Note:

    Ensure that the script is in the same directory as the images or in the system path for it to be executed without specifying the full path.
