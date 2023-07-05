//
//  FirstViewController.m
//  app
//
//  Created by olinone on 2023/7/5.
//

#import "FirstViewController.h"
#import "srcs/SwiftModule/swift_module-Swift.h"

@interface FirstViewController ()

@end

@implementation FirstViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = [UIColor whiteColor];
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    
    SwiftTableViewController *vc = [[SwiftTableViewController alloc] init];
    [self presentViewController:vc animated:YES completion:nil];
}

@end
