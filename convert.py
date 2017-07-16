import os,sys, getopt
list_data = []
input_f = ''
output_f = ''

def read_data_from_binary_file(filename, list_data):
    f = open(filename, 'rb')
    f.seek(0, 0)
    while True:
        t_byte = f.read(1)
        if len(t_byte) == 0:
            break
        else:
            list_data.append("0x%.2X" % ord(t_byte))

def write_data_to_text_file(filename, list_data):
    f_output = open(filename, 'w+')
    f_output.write('const unsigned char temp[] = \n')
    f_output.write('{\n    ')

    count = 0
    lenth = len(list_data)
    for data in list_data:
        count += 1
        if count != lenth:
            f_output.write(data+', ')
        else:
            f_output.write(data)
        if count%16==0:
            f_output.write('\n    ')
    f_output.write('\n};')
    f_output.close()


def main(argv):
    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:",["infile=", "outfile="])
    except getopt.GetoptError:
        print 'Error: test_arg.py -i <inputfile> -o <outputfile>'
        print '   or: test_arg.py --infile=<inputfile> --outfile=<outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            print 'test_arg.py -i <inputfile> -o <outputfile>'
            print 'or: test_arg.py --infile=<inputfile> --outfile=<outputfile>'

            sys.exit()
        elif opt in ("-i", "--infile"):
            inputfile = arg
        elif opt in ("-o", "--outfile"):
            outputfile = arg

    print 'Input file : ', inputfile
    read_data_from_binary_file(inputfile, list_data)
    print 'Output file: ', outputfile
    write_data_to_text_file(outputfile, list_data)

if __name__ == "__main__":
    main(sys.argv[1:])