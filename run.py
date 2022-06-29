import sys

from toyrobot.robot_runner import RobotRunner

if __name__ == "__main__":
    try:
        inputFile = sys.argv[1]
        outputFile = sys.argv[2]
    except IndexError:
        print("Please specify input/output file")
        sys.exit(1)
    RobotRunner.main(inputFile, outputFile)
