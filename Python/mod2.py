
def fileCapitalize(inFilename, outFilename):
    in_file = open(inFilename, 'r') 
    out_file = open(outFilename, 'w')
    for line in in_file:
        out_file.write(line[-1].upper() + '\n')
    in_file.close()
    out_file.close()    


if __name__=="__main__":
    import sys
    # in_args = sys.argv[1:]
    # print(sys.argv)
    # print(in_args)
    if len(sys.argv) > 1:
        in_args = sys.argv[1:]
        inFilename = in_args[0]
        outFilename = in_args[1]
        fileCapitalize(inFilename, outFilename)
    else:
        fileCapitalize('/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/myfile2.txt', '/Users/knu_cgl1/Desktop/Study/Obsidian/Biopython_study/myfile2_cap.txt')