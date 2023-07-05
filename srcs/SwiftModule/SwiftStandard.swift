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
    func with<T>(_ this: T, block: (T) -> () -> T) -> T {
        block(this)()
    }
    
    @inline(__always)
    func apply(block: (Self) -> Void) -> Self {
        block(self)
        return self
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

