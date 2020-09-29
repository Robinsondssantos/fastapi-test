import os, cProfile, pstats


def not_cpu_time():
    times = os.times()
    return times.elapsed - (times.system + times.user)

def profile_not_cpu_time(f, *args, **kwargs):
    prof = cProfile.Profile(not_cpu_time) 
    prof.runcall(f, *args, **kwargs)
    result = pstats.Stats(prof)
    result.sort_stats('time')
    result.print_stats()


def main():
    import urllib
    from urllib import request    

    profile_not_cpu_time(lambda: urllib.request.urlopen('https://pythonspeed.com').read())


if __name__ == '__main__':
    main()


