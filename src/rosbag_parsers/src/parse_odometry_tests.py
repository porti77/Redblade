import rosbag
import argparse


"""
Note:
imu_topic must spit out Vector3Stamped
"""
def parse(bag,out,front_encoder,back_encoder,front_cmd_vel,back_cmd_vel,imu,gps,odom,ekf,ekf2d):
    front_encoder_out = open("%s.front_encoder.csv"%(out),'w')
    back_encoder_out  = open("%s.back_encoder.csv"%(out),'w')
    front_cmd_out     = open("%s.front_cmd_vel.csv"%(out),'w')
    back_cmd_out      = open("%s.back_cmd_vel.csv"%(out),'w')
    imu_out           = open("%s.imu.csv"%(out),'w')
    gps_out           = open("%s.gps.csv"%(out),'w')
    odom_out          = open("%s.odom.csv"%(out),'w')
    ekf_out           = open("%s.ekf.csv"%(out),'w')
    ekf_2d_out        = open("%s.ekf2dpose.csv"%(out),'w')

    for topic,msg,t in bag.read_messages(topics=[front_encoder,back_encoder,front_cmd_vel,back_cmd_vel,imu,gps,odom,ekf,ekf2d]):
        if topic==front_encoder:
            front_encoder_out.write("%d,%d,%f,%d,%d\n"%(msg.header.stamp.secs,
                                                        msg.header.stamp.nsecs,
                                                        msg.encoders.time_delta,
                                                        msg.encoders.left_wheel,
                                                        msg.encoders.right_wheel))
        elif topic==back_encoder:
            back_encoder_out.write("%d,%d,%f,%d,%d\n"%(msg.header.stamp.secs,
                                                       msg.header.stamp.nsecs,
                                                       msg.encoders.time_delta,
                                                       msg.encoders.left_wheel,
                                                       msg.encoders.right_wheel))
        elif topic==front_cmd_vel:
            front_cmd_out.write("%d,%d,%f,%f,%f,%f,%f,%f\n"%(\
                msg.header.stamp.secs,
                msg.header.stamp.nsecs,
                msg.twist.linear.x,
                msg.twist.linear.y,
                msg.twist.linear.z,
                msg.twist.angular.x,
                msg.twist.angular.y,
                msg.twist.angular.z))
        elif topic==back_cmd_vel:
            back_cmd_out.write("%d,%d,%f,%f,%f,%f,%f,%f\n"%(\
                msg.header.stamp.secs,
                msg.header.stamp.nsecs,
                msg.twist.linear.x,
                msg.twist.linear.y,
                msg.twist.linear.z,
                msg.twist.angular.x,
                msg.twist.angular.y,
                msg.twist.angular.z))
        elif topic==imu:
            imu_out.write("%d,%d,%f,%f,%f\n"%(msg.header.stamp.secs,
                                              msg.header.stamp.nsecs,
                                              msg.vector.x,
                                              msg.vector.y,
                                              msg.vector.z))
        elif topic==gps:
            gps_out.write("%d,%d,%f,%f,%f,"%(msg.header.stamp.secs,
                                             msg.header.stamp.nsecs,
                                             msg.pose.pose.position.x,
                                             msg.pose.pose.position.y,
                                             msg.pose.pose.position.z))
            gps_out.write(",".join( map( str ,msg.pose.covariance))+"\n")
        elif topic==odom:
            odom_out.write("%d,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,"%(msg.header.stamp.secs,
                                                                msg.header.stamp.nsecs,
                                                                msg.pose.pose.position.x,
                                                                msg.pose.pose.position.y,
                                                                msg.pose.pose.position.z,
                                                                msg.twist.twist.linear.x,
                                                                msg.twist.twist.linear.y,
                                                                msg.twist.twist.linear.z,
                                                                msg.twist.twist.angular.x,
                                                                msg.twist.twist.angular.y,
                                                                msg.twist.twist.angular.z))
            odom_out.write(",".join( map( str ,msg.pose.covariance))+",")
            odom_out.write(",".join( map( str ,msg.twist.covariance))+"\n")
        elif topic==ekf:
            ekf_out.write("%d,%d,%f,%f,%f,%f,%f,%f,%f,%f,%f,"%(msg.header.stamp.secs,
                                                               msg.header.stamp.nsecs,
                                                               msg.pose.pose.position.x,
                                                               msg.pose.pose.position.y,
                                                               msg.pose.pose.position.z,
                                                               msg.twist.twist.linear.x,
                                                               msg.twist.twist.linear.y,
                                                               msg.twist.twist.linear.z,
                                                               msg.twist.twist.angular.x,
                                                               msg.twist.twist.angular.y,
                                                               msg.twist.twist.angular.z))
            ekf_out.write(",".join( map( str ,msg.pose.covariance))+",")
            ekf_out.write(",".join( map( str ,msg.twist.covariance))+"\n")
        elif topic==ekf2d:
            ekf_2d_out.write("%f,%f,%f\n"%(msg.x,
                                           msg.y,
                                           msg.theta))

    front_encoder_out.close()
    back_encoder_out.close()  
    front_cmd_out.close()                 
    back_cmd_out.close()      
    imu_out.close()           
    gps_out.close()
    odom_out.close()  
    ekf_out.close()   
    ekf_2d_out.close()

    
if __name__=="__main__":
    parser = argparse.ArgumentParser(\
        description="Parses rosbags from odometry tests")
    parser.add_argument(\
        '--input_rosbag',type=str,required=True,default="",
        help='name of input rosbag file')
    parser.add_argument(\
        '--out',type=str,required=False,default="out",
        help='basename of output file(s)')
    parser.add_argument(\
        '--front_encoder_topic',type=str,required=False,default="/encoders_front",
        help='name of front encoder topic')
    parser.add_argument(\
        '--back_encoder_topic',type=str,required=False,default="/encoders_back",
        help='name of back encoder topic')
    parser.add_argument(\
        '--front_cmd_vel_topic',type=str,required=False,default="/roboteq_front/cmd_vel_stamped",
        help='name of front cmd_vel topic')
    parser.add_argument(\
        '--back_cmd_vel_topic',type=str,required=False,default="/roboteq_back/cmd_vel_stamped",
        help='name of back cmd_vel topic')
    parser.add_argument(\
        '--imu_topic',type=str,required=False,default="/imu/integrated_gyros_stamped",
        help='name of imu topic')
    parser.add_argument(\
        '--gps_topic',type=str,required=False,default="/gps",
        help='name of gps topic')
    parser.add_argument(\
        '--odom_topic',type=str,required=False,default="/odom",
        help='name of odom topic')
    parser.add_argument(\
        '--ekf_topic',type=str,required=False,default="/redblade_ekf/odom",
        help='name of ekf topic')
    parser.add_argument(\
        '--ekf_2d_topic',type=str,required=False,default="/redblade_ekf/2d_pose",
        help='name of ekf topic')
    args = parser.parse_args()
        
    bag = rosbag.Bag(args.input_rosbag)
    parse(bag,
          args.out,
          args.front_encoder_topic,
          args.back_encoder_topic,
          args.front_cmd_vel_topic,
          args.back_cmd_vel_topic,
          args.imu_topic,
          args.gps_topic,
          args.odom_topic,
          args.ekf_topic,
          args.ekf_2d_topic)
