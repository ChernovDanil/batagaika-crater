import batagaika_gif as bg


def main():
    frames_list = bg.create_frames('frames/')
    duration = 250
    bg.create_gif(f'gifs/batagika_crater_2014-2023_{duration}ms.gif', frames_list, duration, 0)


if __name__ == '__main__':
    main()
