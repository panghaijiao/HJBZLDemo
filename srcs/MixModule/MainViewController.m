//
//  MainViewController.m
//  app
//
//  Created by olinone on 2023/7/5.
//

#import "MainViewController.h"
#import "srcs/SwiftModule/swift_module-Swift.h"
#import "srcs/MixModule/mix_module-Swift.h"

@interface MainViewController ()

@end

@implementation MainViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = [UIColor whiteColor];
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    
    MixSwiftViewController *vc = [[MixSwiftViewController alloc] init];
    [self presentViewController:vc animated:YES completion:nil];
}

@end