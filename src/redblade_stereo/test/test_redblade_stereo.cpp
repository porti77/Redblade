#include <gtest/gtest.h>
#include "redblade_stereo.h"

TEST(redblade_stereo,testFilterGround1){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    above(new pcl::PointCloud<pcl::PointXYZ>());
  cloud->width = 100;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 0; i<cloud->points.size(); ++i){
    cloud->points[i].x = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].y = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].z = 1024*rand()/(RAND_MAX+1.0f);
  }
  redblade_stereo testRS(radius,height,width);
  testRS.filterGround(cloud,above);
  EXPECT_GT(above->points.size(),0);
  for(size_t i = 0; i<above->points.size();i++){
    EXPECT_GT(above->points[i].y,-1*height);
  }
}

TEST(redblade_stereo,testFilterBackground1){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    above(new pcl::PointCloud<pcl::PointXYZ>());
  cloud->width = 100;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 0; i<cloud->points.size(); ++i){
    cloud->points[i].x = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].y = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].z = 1024*rand()/(RAND_MAX+1.0f);
  }
  redblade_stereo testRS(radius,height,width);
  testRS.filterGround(cloud,above);
  EXPECT_GT(above->points.size(),0);
  for(size_t i = 0; i<above->points.size();i++){    
    double distance =					\
      sqrt((above->points[i].x*above->points[i].x)+	\
	   (above->points[i].y*above->points[i].y)+	\
	   (above->points[i].z*above->points[i].z));    
    EXPECT_LT(distance,2*radius);
  }
}


TEST(redblade_stereo,testRansac){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    line(new pcl::PointCloud<pcl::PointXYZ>());
  Eigen::VectorXf coeff;
  //pcl::PointCloud<pcl::PointXYZ>::Ptr cloud,line;
  cloud->width = 100;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 0; i<cloud->points.size(); ++i){//Place everything on a line
    cloud->points[i].x = 1;
    cloud->points[i].y = i+10;
    cloud->points[i].z = 1;
  }
  redblade_stereo testRS(radius,height,width);
  testRS.ransac(cloud,line,coeff);
  EXPECT_EQ(cloud->points.size(),line->points.size());
}


TEST(redblade_stereo,testRansac2){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    line(new pcl::PointCloud<pcl::PointXYZ>());
  Eigen::VectorXf coeff;
  cloud->width = 100;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 0; i<50; ++i){//Place straight line
    cloud->points[i].x = 0;
    cloud->points[i].y = i+10;
    cloud->points[i].z = 0;    
  }
  for(size_t i = 50; i<cloud->points.size(); ++i){
    cloud->points[i].x = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].y = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].z = 1024*rand()/(RAND_MAX+1.0f);
  }
  redblade_stereo testRS(radius,height,width);
  testRS.ransac(cloud,line,coeff);
  EXPECT_GT(line->points.size(),49);
}


TEST(redblade_stereo,testFindPole1){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    line(new pcl::PointCloud<pcl::PointXYZ>());
  cloud->width = 300;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 0; i<200; ++i){//Place straight line
    cloud->points[i].x = 0;
    cloud->points[i].y = i+10;
    cloud->points[i].z = 0;    
  }
  for(size_t i = 200; i<cloud->points.size(); ++i){
    cloud->points[i].x = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].y = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].z = 1024*rand()/(RAND_MAX+1.0f);
  }
  redblade_stereo testRS(radius,height,width);
  testRS.findPole(cloud,line);
  EXPECT_GT(line->points.size(),150);
}

TEST(redblade_stereo,testFindPole2){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    line(new pcl::PointCloud<pcl::PointXYZ>());
  cloud->width = 300;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 300; i<cloud->points.size(); ++i){
    cloud->points[i].x = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].y = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].z = 1024*rand()/(RAND_MAX+1.0f);
  }
  redblade_stereo testRS(radius,height,width);
  bool result = testRS.findPole(cloud,line);
  EXPECT_FALSE(result);
}

TEST(redblade_stereo,testFindPole3){
  double radius = 1.0;
  double height = 1.0;
  double width = 0.05;
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    cloud(new pcl::PointCloud<pcl::PointXYZ>());
  boost::shared_ptr<pcl::PointCloud<pcl::PointXYZ> > 
    line(new pcl::PointCloud<pcl::PointXYZ>());
  cloud->width = 300;
  cloud->height = 1;
  cloud->points.resize(cloud->width*cloud->height);
  for(size_t i = 0; i<50; ++i){//Place straight line
    cloud->points[i].x = 0;
    cloud->points[i].y = i+10;
    cloud->points[i].z = 0;    
  }
  for(size_t i = 50; i<cloud->points.size(); ++i){
    cloud->points[i].x = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].y = 1024*rand()/(RAND_MAX+1.0f);
    cloud->points[i].z = 1024*rand()/(RAND_MAX+1.0f);
  }
  redblade_stereo testRS(radius,height,width);
  bool result = testRS.findPole(cloud,line);
  EXPECT_FALSE(result);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}