def main():
    ranges = []

    n = 0
    num_of_p = 0
    while n < 16860:
        ranges.append((n+18.1-0.4, n+18.1+0.4))
        n += 18.1
        num_of_p += 1

    total_pitch = 0
    covered_len = 0

    while ranges:
        cur_range = ranges.pop(0)
        
        cur_len = cur_range[0] - covered_len
        
        if cur_len % 2.15 <= 1.35:
            num_pitch = cur_len // 2.15 
            covered_len += 2.15 * num_pitch
        else:
            num_pitch = cur_len // 2.15 + 1
            covered_len = cur_range[0]
            
        total_pitch += num_pitch

    print(' Total number of pitches: {}'.format(total_pitch), 
          '\n',
          'Covered Length: {}'.format(covered_len))

if __name__ == '__main__':
    main()

    