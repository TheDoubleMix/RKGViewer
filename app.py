from os import system
from os.path import splitext, isfile
from sys import argv
from colorama import init as colorama_init
from colorama import Fore, Style, Back
from platform import system as s2
linux = s2() == 'Linux'
windows = s2() == 'Windows'
if linux:
    from curtsies import Input
else:
    from keyboard import is_pressed
colorama_init()
tracks = ["Mario Circuit", "Moo Moo Meadows", "Mushroom Gorge", "Grumble Volcano", "Toad's Factory", "Coconut Mall", "DK's Snowboard Cross/DK Summit", "Wario's Gold Mine", "Luigi Circuit", "Daisy Circuit", "Moonview Highway", "Maple Treeway", "Bowser's Castle", "Rainbow Road", "Dry Dry Ruins", "Koopa Cape", "GCN Peach Beach", "GCN Mario Circuit", "GCN Waluigi Stadium", "GCN DK Mountain", "DS Yoshi Falls", "DS Desert Hills", "DS Peach Gardens", "DS Delfino Square", "SNES Mario Circuit 3", "SNES Ghost Valley 2", "N64 Mario Raceway", "N64 Sherbet Land", "N64 Bowser's Castle", "N64 DK's Jungle Parkway", "GBA Bowser's Castle 3", "GBA Shy Guy Beach", "Delfino Pier", "Block Plaza", "Chain Chomp Roulette/Chain Chomp Wheel", "Funky Stadium",  "Thwomp Desert", "GCN Cookie land", "DS Twilight House", "SNES Battle Course 4", "GBA Battle Course 3", "N64 Skyscraper", "???", "???", "???", "???", "???", "???", "???", "???", "???", "???", "???", "???", "Galaxy Arena/Galaxy Colosseum", "winningrun_demo", "loser_demo", "draw_demo", "ending_demo"]
Vehicles = ["Standard Kart S", "Standard Kart M", "Standard Kart L", "Baby Booster/Booster Seat", "Nostalgia 1/Classic Dragster", "Offroader", "Concerto/Mini Beast", "Wild Wing", "Flame Flyer", "Cheep Charger", "Turbo Blooper/Super Blooper", "Piranha Prowler", "Rally Romper/Tiny Titan", "Royal Racer/Daytripper", "Aero Glider/Jetsetter", "Blue Falcon", "B Dasher Mk.2/Sprinter", "Dragonetti/Honeycoupe", "Standard Bike S", "Standard Bike M", "Standard Bike L", "Bullet Bike", "Mach Bike", "Bowser Bike/Flame Runner", "Nanobike/Bit Bike", "Bon Bon/Shugarscoot", "Wario Bike", "Quacker", "Rapide/Zip Zip", "Twinkle Star/Shooting Star", "Magikruiser", "Nitrocycle/Sneakster", "Torpedo/Spear", "Bubble Bike/Jet Bubble", "Dolphin Dasher", "Phantom"]
Characters = ["Mario", "Baby Peach", "Waluigi", "Bowsers", "Baby Daisy", "Dry Bones", "Baby Mario", "Luigi", "Toad", "Donkey Kong", "Yoshi", "Wario", "Baby Luigi", "Toadette", "Koopa Troopa", "Daisy", "Peach", "Birdo", "Diddy Kong", "King Boo", "Bowser Jr.", "Dry Bowser", "Funky Kong", "Rosalina", "Small Mii Outfit A (Male)", "Small Mii Outfit A (Female)", "Small Mii Outfit B (Male)", "Small Mii Outfit B (Female)", "Small Mii Outfit C (Male)", "Small Mii Outfit C (Female)", "Medium Mii Outfit A (Male)", "Medium Mii Outfit A (Female)", "Medium Mii Outfit B (Male)", "Medium Mii Outfit B (Female)", "Medium Mii Outfit C (Male)", "Medium Mii Outfit C (Female)", "Large Mii Outfit A (Male)", "Large Mii Outfit A (Female)", "Large Mii Outfit B (Male)", "Large Mii Outfit B (Female)", "Large Mii Outfit C (Male)", "Large Mii Outfit C (Female)", "Medium Mii", "Small Mii", "Large Mii"]
Controllers = ["Wii Wheel", "Wii Remote + Nunchuck", "Classic Controller", "GameCube"]
ghosttypes = ["A Player's best time", "World Record Ghost", "Continental Record Ghost", "Rival Ghost", "Special Ghost", "Ghost Race", "Friend Ghost 1", "Friend Ghost 2", "Friend Ghost 3", "Friend Ghost 4", "Friend Ghost 5", "Friend Ghost 6", "Friend Ghost 7", "Friend Ghost 8", "Friend Ghost 9", "Friend Ghost 10", "Friend Ghost 11", "Friend Ghost 12", "Friend Ghost 13", "Friend Ghost 14", "Friend Ghost 15", "Friend Ghost 16", "Friend Ghost 17", "Friend Ghost 18", "Friend Ghost 19", "Friend Ghost 20", "Friend Ghost 21", "Friend Ghost 22", "Friend Ghost 23", "Friend Ghost 24", "Friend Ghost 25", "Friend Ghost 26", "Friend Ghost 27", "Friend Ghost 28", "Friend Ghost 29", "Friend Ghost 30", "Normal Staff Ghost", "Expert Staff Ghost"]
def clear() -> None:
    if windows: # Windows
        system('cls')
    else: # Mac/Linux
        system('clear')
clear()
def get_file() -> str:
    error = ""
    while True:
        if not error == "":
            print(Fore.RED + "Please give a valid rkg file. " + error + Style.RESET_ALL)
        print("Type \"exit\" to exit rkgview")
        rkgfile = input("Give a path to a rkg file:")
        if rkgfile.lower() == "exit":
            file = "EXIT"
            break
        extention = splitext(rkgfile)[1].removeprefix(".")
        if not isfile(rkgfile):
            clear()
            error = "File doesn't exist!"
        elif extention.lower() == "rkg":
            clear()
            file = rkgfile
            print("hello")
            break
        else:
            clear()
            print(Fore.RED + "Expected header \"rkg\", got \"" + extention.lower() + "\"." + Style.RESET_ALL)
            ans = input("Do you still want to use this file? [Y/N]: ").lower()[0]
            if ans == "y":
                file = rkgfile
                break
    return file
class Yaz1dec:
    @classmethod
    def decode_all(self, src: bytes) -> bytearray:
        read_bytes = 0
        src_size = len(src)
        decoded_bytes = bytearray()
        while read_bytes < src_size:
            while (read_bytes + 3 < src_size and
                   (src[read_bytes] != ord('Y') or
                    src[read_bytes + 1] != ord('a') or
                    src[read_bytes + 2] != ord('z') or
                    src[read_bytes + 3] != ord('1'))):
                read_bytes += 1
            if read_bytes + 3 >= src_size:
                return decoded_bytes
            read_bytes += 4
            size = int.from_bytes(src[read_bytes:read_bytes + 4], byteorder='big')
            dst = bytearray(size + 0x1000)
            read_bytes += 12
            src_pos, _ = self.decode_yaz1(src, read_bytes, src_size - read_bytes, dst, size)
            read_bytes += src_pos
            decoded_bytes.extend(dst[:size])
        return decoded_bytes
    @classmethod
    def decode_yaz1(self, src: bytes, offset: int, src_size: int, dst: bytearray, uncompressed_size: int) -> tuple[int, int]:
        src_pos, dst_pos = 0, 0
        valid_bit_count = 0
        curr_code_byte = src[offset + src_pos]
        while dst_pos < uncompressed_size:
            if valid_bit_count == 0:
                curr_code_byte = src[offset + src_pos]
                src_pos += 1
                valid_bit_count = 8
            if (curr_code_byte & 0x80) != 0:
                dst[dst_pos] = src[offset + src_pos]
                dst_pos += 1
                src_pos += 1
            else:
                byte1 = src[offset + src_pos]
                byte2 = src[offset + src_pos + 1]
                src_pos += 2
                dist = ((byte1 & 0xF) << 8) | byte2
                copy_source = dst_pos - (dist + 1)
                num_bytes = byte1 >> 4
                if num_bytes == 0:
                    num_bytes = src[offset + src_pos] + 0x12
                    src_pos += 1
                else:
                    num_bytes += 2
                for _ in range(num_bytes):
                    dst[dst_pos] = dst[copy_source]
                    copy_source += 1
                    dst_pos += 1
            curr_code_byte <<= 1
            valid_bit_count -= 1
        return src_pos, dst_pos
def main(file: str) -> None:
    if file == "EXIT":
        return None
    with open(file, 'rb') as f:
        _bytes = f.read()
    bits = ''.join(f'{z:08b}' for z in _bytes)
    def read_bits(offset: int, size: int) -> str:
        return bits[offset:offset+size]
    header = read_bits(0, 32)
    correctheader = "01010010010010110100011101000100"
    if not header == correctheader:
        counter = 0
        for character in header:
            if character == correctheader[counter]:
                print(Fore.GREEN + character + Style.RESET_ALL, end="")
            else:
                print(Fore.RED + character + Style.RESET_ALL, end="")
            counter += 1
        print(Fore.BLUE + " "*10 + "First 32 bits" + Style.RESET_ALL)
        print(Fore.BLUE + correctheader + " "*11 + "Correct bits" + Style.RESET_ALL + "\nThe header of this rkg file seems to be corrupted.")
        ans = input("Do you still want to use this file? [Y/N]:").lower()[0]
        if ans == "n":
            return None
    clear()
    m = str(int(read_bits(32, 7), 2))
    s = str(int(read_bits(39, 7), 2))
    ms = str(int(read_bits(46, 10), 2))
    trackid = int(read_bits(56, 6), 2)
    vehicleid = int(read_bits(64, 6), 2)
    charid = int(read_bits(70, 6), 2)
    year = str(int(read_bits(76, 7), 2) + 2000)
    month = str(int(read_bits(83, 4), 2))
    day = str(int(read_bits(87, 5), 2))
    controllerid = int(read_bits(92, 4), 2)
    if read_bits(100, 1) == "1":
        Compressed = True
    else:
        Compressed = False
    ghosttype = int(read_bits(103, 7), 2)
    inputlen = str(int(read_bits(112, 16), 2))
    laps = str(int(read_bits(128, 8), 2))
    if read_bits(110, 1) == "1":
        drifttype = "Automatic"
    else:
        drifttype = "Manual"
    lap_times = []
    _offset = 136
    for _ in range(5):
        for _ in range(2):
            if len(str(int(read_bits(_offset, 7), 2))) == 1:
                lap_times.append("0" + str(int(read_bits(_offset, 7), 2)))
            else:
                lap_times.append(str(int(read_bits(_offset, 7), 2)))
            _offset += 7
        if len(str(int(read_bits(_offset, 10), 2))) == 1:
            lap_times.append("00" + str(int(read_bits(_offset, 10), 2)))
        elif len(str(int(read_bits(_offset, 10), 2))) == 2:
            lap_times.append("0" + str(int(read_bits(_offset, 10), 2)))
        else:
            lap_times.append(str(int(read_bits(_offset, 10), 2)))
        _offset += 10
    input_amount = int(read_bits(1088, 32), 2)
    decompress_size = int(read_bits(1152, 32), 2)
    decompressed = bytes(Yaz1dec.decode_all(_bytes[140:decompress_size]))
    if len(s) == 1:
        s = "0" + s
    if len(ms) == 1:
        ms = "00" + ms
    elif len(ms) == 2:
        ms = "0" + ms
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    if len(m) == 1:
        m = "0" + m
    class menu:
        ESC: str = "\nPress ESC to quit this menu."
        @classmethod
        def menu(self):
            in_menu = False
            print("> Info\n  Inputs\n  Misc\n  Options\nPress ESC to quit/→ to select.")
            cursor = 0
            def select():
                if cursor % 4 == 0:
                    print(self.info(), end="")
                elif cursor % 4 == 1:
                    print(self.inputs(), end="")
                elif cursor % 4 == 2:
                    print(self.misc_info(), end="")
                elif cursor % 4 == 3:
                    print(self.options(), end="")
            def update():
                if cursor % 4 == 0:
                    print("> Info\n  Inputs\n  Misc\n  Options")
                elif cursor % 4 == 1:
                    print("  Info\n> Inputs\n  Misc\n  Options")
                elif cursor % 4 == 2:
                    print("  Info\n  Inputs\n> Misc\n  Options")
                elif cursor % 4 == 3:
                    print("  Info\n  Inputs\n  Misc\n> Options")
                print("Press ESC to quit/→ to select.")
            if linux:
                with Input() as input_generator:
                    for e in input_generator:
                        if not in_menu:
                            if e in (u'<ESC>'):
                                return None
                            if e in (u'<UP>'):
                                clear()
                                cursor -= 1
                                update()
                            if e in (u'<DOWN>'):
                                clear()
                                cursor += 1
                                update()
                            if e in (u'<RIGHT>'):
                                clear()
                                select()
                                in_menu = True
                        else:
                            if e in (u'<ESC>'):
                                clear()
                                cursor = 0
                                print("> Info\n  Inputs\n  Misc\n  Options\nPress ESC to quit/→ to select.")
                                in_menu = False
            else:
                def wait_until_not(key):
                    while is_pressed(key):
                        if not is_pressed(key):
                            break
                while True:
                    if not in_menu:
                        if is_pressed("esc"):
                            return None
                        if is_pressed("up"):
                            clear()
                            cursor -= 1
                            update()
                            wait_until_not("esc")
                        if is_pressed("down"):
                            clear()
                            cursor += 1
                            update()
                            wait_until_not("down")
                        if is_pressed("right"):
                            clear()
                            select()
                            in_menu = True
                            wait_until_not("right")
                    else:
                        if is_pressed("esc"):
                            clear()
                            cursor = 0
                            print("> Info\n  Inputs\n  Misc\n  Options\nPress ESC to quit/→ to select.")
                            in_menu = False
                            wait_until_not("esc")
        @classmethod
        def info(self) -> str:
            metadata_str = "Info".center(20) + "\n" + "-"*20
            time_str = "\nTime: " + m + ":" + s + "." + ms
            misc_str = "\nTrack: " + tracks[trackid] + "\nCharacter: " + Characters[charid] +"\nVehicle: " + Vehicles[vehicleid]
            drift_str = "\nDrift type: " + drifttype
            
            date_str = "\nDate: " + year + "/" + month + "/" + day
            ctrler_str = "\nController: " + Controllers[controllerid % 5]
            lap_splits = "\n"
            for i in range(1, int(laps) + 1):
                if i != int(laps) + 1:
                    lap_splits += "Lap " + str(i) + " Time: " + lap_times[(i*3)-3] + ":" + lap_times[(i*3)-2] + "." + lap_times[(i*3)-1] + "\n"
                else:
                    lap_splits += "Lap " + str(i) + " Time: " + lap_times[(i*3)-3] + ":" + lap_times[(i*3)-2] + "." + lap_times[(i*3)-1]
            
            #print(" ――――――――――――――\n│              │\n│              │\n│          .˙· │\n│              │\n│          .˙· │\n ‾‾‾‾‾‾‾‾‾‾‾‾‾‾") square lol
            return metadata_str + time_str + lap_splits + misc_str + drift_str + date_str + ctrler_str + self.ESC
        @classmethod
        def misc_info(self):
            misc2_str = "Ghost type: " + str(hex(ghosttype)) + " (" + ghosttypes[ghosttype - 1] + ")"
            misc3_str = "\nInput data length decompressed: " + inputlen + " Bytes\nLaps Driven: " + laps + "\nCompressed: " + str(Compressed)
            return misc2_str + misc3_str + self.ESC
        @classmethod
        def inputs(self) -> None:
            raise NotImplemented
        def options(self) -> None:
            raise NotImplemented
    menu.menu()
    #print(lap_times)
if len(argv) < 2:
    print(Fore.RED + "No RKG File argument given!" + Style.RESET_ALL)
    main(get_file())
elif len(argv) > 2:
    print(Fore.RED + "Too Many arguments!\n" + Fore.BLUE + "If you want to you can still select the file you want to choose." + Style.RESET_ALL)
    main(get_file())
else:
    print(Fore.BLUE + "Using second argument as rkg file" + Style.RESET_ALL)
    extention = splitext(argv[1])[1].removeprefix(".")
    if not isfile(argv[1]):
        print("File doesn't exist!")
        file = get_file()
        clear()
    elif extention.lower() == "rkg":
        file = argv[1]
    else:
        print(Fore.RED + "Expected header \"rkg\", got \"" + extention.lower() + "\"." + Style.RESET_ALL)
        ans = input("Do you still want to use this file? [Y/N]: ").lower()[0]
        if ans == "y":
            file = argv[1]
        else:
            file = get_file()
        clear()
    main(file)
