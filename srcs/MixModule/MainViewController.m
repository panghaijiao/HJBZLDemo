//
//  MainViewController.m
//  HJBZLDemo
//
//  Created by olinone on 2023/7/5.
//

#import "MainViewController.h"
#import "srcs/SwiftModule/swift_module-Swift.h"
#import "srcs/MixModule/MixModule-Swift.h"
#import <Masonry/Masonry.h>
#import <OCModule/OCModule.h>

@interface MainViewController ()

@end

@implementation MainViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    self.view.backgroundColor = [UIColor redColor];
}

- (void)viewDidAppear:(BOOL)animated {
    [super viewDidAppear:animated];
    
    MixSwiftViewController *swiftVC = [MixSwiftViewController new];
    SwiftTableViewController *vc = [SwiftTableViewController new];
    [self presentViewController:vc animated:YES completion:nil];
}

@end
