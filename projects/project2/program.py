import time
from projects.project2.kbhit import KBHit


def main():
    
    print("Hello, World!")
    kb = KBHit()

    print('Hit any key, or ESC to exit')

    iteration = 0

    while True:

        print(f'In loop: {iteration}')
        iteration += 1
        time.sleep(1)

        if kb.kbhit():
            key = (kb.getch())
            print(f'Key you pressed is {key}')
            time.sleep(2)
            if key == "Q": # ESC
                break
            

    kb.set_normal_term()


if __name__ == '__main__':
    main()
