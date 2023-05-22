import wpilib


#from autoroutine import AutoRoutine
#from drivestraight import DriveStraight
from drivetrain import Drivetrain
#from gyroturn import GyroTurn
from commands.drivedistance import DriveDistance
import commands2
import commands2.button
from commands.arcadedrive import ArcadeDrive
class RobotContainer:

    def __init__(self) -> None:
        self.controller = wpilib.Joystick(0)
        # Create SmartDashboard chooser for autonomous routines
        self.chooser = wpilib.SendableChooser()
        self.drivetrain = Drivetrain()
        self._configure()

    def _configure(self):
        self.chooser.setDefaultOption("Drive Distance", DriveDistance(.5, .3, self.drivetrain))
#        self.chooser.addOption("Go straight 2m", DriveStraight(self.drivetrain, 2))
        wpilib.SmartDashboard.putData(self.chooser)
        self.drivetrain.setDefaultCommand(self.getArcadeDriveCommand())

    def get_autonomous(self):
        return self.chooser.getSelected()
    def getArcadeDriveCommand(self) -> ArcadeDrive:
        """Use this to pass the teleop command to the main robot class.

        :returns: the command to run in teleop
        """
        return ArcadeDrive(
            self.drivetrain,
            lambda: self.controller.getRawAxis(0),
            lambda: self.controller.getRawAxis(1),
        )