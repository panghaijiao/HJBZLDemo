load("@rules_cc//cc:defs.bzl", "objc_library")

package(default_visibility = ["//visibility:public"])

filegroup(
    name = "package-srcs",
    srcs = glob(["**"]),
    tags = ["automanaged"],
    visibility = ["//visibility:private"],
)

filegroup(
    name = "all-srcs",
    srcs = [
        ":package-srcs",
    ],
    tags = ["automanaged"],
    visibility = ["//visibility:public"],
)

objc_library(
    name = "Masonry_library",    
    hdrs = glob(["Public/**/*.h"]),
    srcs = glob(["Masonry/**/*.m"]),
    copts = [
        "-iquote srcs/base/Masonry/Public/Masonry",
    ],
    includes = ["Public"],
)
