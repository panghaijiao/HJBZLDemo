load("@build_bazel_rules_swift//swift:swift.bzl", "swift_library")

package(default_visibility = [
    "//visibility:public"
])

swift_library(
    name = "swift_module",
    module_name = "SwiftModule",
    copts = ["-no-warnings-as-errors"],
    generates_header = True,
    srcs = glob([
        "**/*.swift",
    ]),
    deps = [
        "//srcs/base/Masonry:Masonry_library",
        # "@rxswift//:RxCocoa",
    ],
)
