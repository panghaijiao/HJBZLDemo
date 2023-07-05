load("@rules_cc//cc:defs.bzl", "objc_library")
load("@build_bazel_rules_apple//apple:apple.bzl", "experimental_mixed_language_library")

package(default_visibility = [
    "//visibility:public"
])

experimental_mixed_language_library(
    name = "mix_module",
    hdrs = glob([
        "**/*.h",
    ]),
    srcs = glob([
        "**/*.m",
        "**/*.swift",
    ]),
    deps = [
        "//srcs/base/Masonry:Masonry_library",
        "//srcs/SwiftModule:swift_module",
    ],
)
