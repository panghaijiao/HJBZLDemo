//
//  SwiftTableViewController.swift
//  app
//
//  Created by olinone on 2023/7/5.
//

import Foundation
import UIKit
import Masonry

@objcMembers
public class SwiftTableViewController : UIViewController {
    
    public override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .blue
        setupUI()
    }
    
    // MARK: UI
    
    private func setupUI() {
        view.addSubview(tableView)
        if let maker = tableView.mas_makeConstraints() {
            maker.edges.mas_equalTo()(self.view)
            maker.install()
        }
    }
    
    // MARK: View
    
    private lazy var tableView = UITableView(frame: .zero, style: .plain).apply { v in
        v.backgroundColor = .clear
        v.delegate = self
        v.dataSource = self
        v.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
    }
}

extension SwiftTableViewController : UITableViewDelegate {
    
    public func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
    }
    
}

extension SwiftTableViewController : UITableViewDataSource {
    public func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return 10
    }
    
    public func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        if let cell = tableView.dequeueReusableCell(withIdentifier: "Cell") {
            cell.textLabel?.text = "\(indexPath.row)"
            cell.backgroundColor = .clear
            return cell
        }
        return UITableViewCell()
    }
}
