import rospy
import numpy as np
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

class Interface:

    ## Robot joint states
    joint_states_ = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    ## Robot joint state ROS message
    joint_state_msg_ = JointState()

    ## Joint command publisher
    publisher_joint_command_ = rospy.Publisher('/robot_joint_command', JointState, queue_size=1)

    ## Interface constructor
    # @param self The object pointer
    # @param dof Number of degrees of freedom
    def __init__(self, dof):
        self.dof_ = dof
        self.publisher_joint_command_ = rospy.Publisher('/robot_joint_command', JointState, queue_size=1)
        self.subscriber_joint_state_ = rospy.Subscriber('/robot_joint_state', JointState, self.joint_positions_callback)

    ## Send joint positions to robot
    # @param joint_positions The robot joint positions
    def send_joint_position(self, joint_positions):
        joint_command = np.zeros(self.dof_)
        self.joint_state_msg_.header = Header()
        self.joint_state_msg_.header.stamp = rospy.Time.now()
        self.joint_state_msg_.name = ['joint0', 'joint1', 'joint2', 'joint3', 'joint4', 'joint5', 'joint6']
        for ii in range(self.dof_):
            joint_command[ii] = joint_positions[ii]
        self.joint_state_msg_.position = joint_command
        self.joint_state_msg_.velocity = []
        self.joint_state_msg_.effort = []
        self.publisher_joint_command_.publish(self.joint_state_msg_)

    ## Get robot joint positions
    def get_joint_positions(self):
        return self.joint_states_

    ## ROS callback method for robot joint positions
    # @param data is the JointStates ROS message
    def joint_positions_callback(self, data):
        for ii in range(len(data.position)):
            self.joint_states_[ii] = data.position[ii]





