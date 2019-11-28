for case in range(int(input())):
    num_words = int(input())
    words = [input() for x in range(num_words)]
    practiced_words = {}
    time = 0
    for i in words:
        if i in practiced_words:
            time += practiced_words[i] / 2
        else:
            _time = 2
            z = i.replace('j', 'k').replace('f', 'd')
            for xyz in range(1, len(z)):
                if z[xyz] == z[xyz - 1]:
                    _time += 4
                else:
                    _time += 2
            practiced_words[i] = _time
            time += _time
    print(int(time))
