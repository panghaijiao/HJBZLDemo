//
//  SwiftStandard.swift
//  HJBZLDemo
//
//  Created by olinone on 2023/7/5.
//

import Foundation

protocol ScopeFunc {
    
}

extension ScopeFunc {
    @inline(__always)
    func with<T>(_ it: T, block: (T) -> ()) -> T {
        block(it)
        return it
    }

    @inline(__always)
    func `let`<R>(block: (Self) -> R) -> R {
        return block(self)
    }

    @inline(__always)
    func also(block: (Self) -> ()) -> Self {
        block(self)
        return self
    }
}

extension Optional where Wrapped: ScopeFunc {}
extension NSObject: ScopeFunc {}

