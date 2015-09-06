//
//  ViewController.swift
//  TestAppium
//
//  Created by Alejandro Barros on 15/08/15.
//  Copyright (c) 2015 Alejandro Barros Cuetos. All rights reserved.

//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are met:
//
//  1. Redistributions of source code must retain the above copyright notice, this
//  list of conditions and the following disclaimer.
//
//  2. Redistributions in binary form must reproduce the above copyright notice,
//  this list of conditions and the following disclaimer in the documentation
//  && and/or other materials provided with the distribution.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
//  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
//  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
//  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
//  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
//  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
//  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
//  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
//  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
//  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
//  POSSIBILITY OF SUCH DAMAGE.
//


import UIKit

class ViewController: UIViewController {

    // MARK: - Outlets
    
    @IBOutlet weak var textField1: UITextField!
    @IBOutlet weak var textField2: UITextField!
    
    // MARK: - Actions

    @IBAction func clearAction(sender: UIButton) {
        
        textField1.text = ""
        textField2.text = ""
    }
    
    @IBAction func submitAction(sender: UIButton) {
        
        let alertController: UIAlertController = UIAlertController(title: "Submission Message", message: "textfield1: \(textField1.text) textfield2: \(textField2.text)", preferredStyle: .Alert)
        alertController.accessibilityLabel = "SubmitAlertController"
        alertController.addAction(UIAlertAction(title: "ok", style: .Cancel, handler: nil))
        presentViewController(alertController, animated: true, completion: nil)
    }
}

