# Starter Robot Code
import os

import wpilib
import commands2
#from wpilib import TimedRobot

from robotcontainer import RobotContainer


class Robot(commands2.TimedCommandRobot):

    def robotInit(self) -> None:
        self.container = RobotContainer()

    #def robotPeriodic(self) -> None:
    #    ...

    def teleopInit(self) -> None:
        if self.autonomousCommand:
            self.autonomousCommand.cancel()

    def teleopPeriodic(self) -> None:
        #forward = self.container.controller.getRawAxis(0)
        #rotate = self.container.controller.getRawAxis(1)
        #self.container.drivetrain.arcadeDrive(rotate, forward)
        #print(f"Forward: {forward}, Rotate: {rotate}")
        pass

    def autonomousInit(self) -> None:
        #self.auto = self.container.get_autonomous()
        self.autonomousCommand = self.container.get_autonomous()

        if self.autonomousCommand:
            self.autonomousCommand.schedule()


    def autonomousPeriodic(self) -> None:
        #self.auto.run()
        pass

    def autonomousExit(self) -> None:
        #self.container.drivetrain.resetGyro()
        pass

    def disabledInit(self) -> None:
        pass


if __name__ == "__main__":
    os.environ["HALSIMWS_HOST"] = "10.0.0.2"
    os.environ["HALSIMWS_PORT"] = "3300"

    wpilib.run(Robot)
