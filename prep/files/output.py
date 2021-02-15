def output_to_filename(state, filename):
    """Outputs the state information to the filename."""
    f = open(filename, 'w')
    f.write('{} {}'.format(state.a, state.b))
    f.write('\nA Values:')
    for elem in state.a_values:
        f.write('\n{} {} {}'.format(elem[0], elem[1], elem[2]))
    f.write('\nB Values:')
    for elem in state.b_values:
        f.write('\n{} {}'.format(elem[0], elem[1]))

    f.close()
