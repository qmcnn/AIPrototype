$(function () {
    var editingEnabled = true;
    $("#spreadsheet").igSpreadsheet({
        height: "600",
        width: "100%",
        isFormulaBarVisible: true,
        editModeEntering: function (e, args) {
            return editingEnabled;
        }
    });

    $("#enableEditing").igCheckboxEditor({
        checked: true,
        valueChanged: function (evt, ui) {
            editingEnabled = ui.newState;
        }
    });

    //Check for Browser's - File API support
    if (window.FileReader) {
        $("#input").on("change", function () {
            var excelFile,
                fileReader = new FileReader();

            $("#result").hide();

            fileReader.onload = function (e) {
                var buffer = new Uint8Array(fileReader.result);

                $.ig.excel.Workbook.load(buffer, function () {
                    workbook = arguments[0];
                    setWorkbook();

                }, function (error) {
                    $("#result").text("The excel file is corrupted.");
                    $("#result").show(1000);
                });
            }

            if (this.files.length > 0) {
                excelFile = this.files[0];
                if (excelFile.type === "application/vnd.ms-excel" || excelFile.type === "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" || (excelFile.type === "" && (excelFile.name.endsWith("xls") || excelFile.name.endsWith("xlsx")))) {
                    fileReader.readAsArrayBuffer(excelFile);
                } else {
                    $("#result").text("The format of the file you have selected is not supported. Please select a valid Excel file ('.xls, *.xlsx').");
                    $("#result").show(1000);
                }
            }
        })
    } else {
        $("#result").text("The File APIs are not fully supported in this browser.");
        $("#result").show(1000);
    }
});

function setWorkbook() {
    if ($("#spreadsheet").igSpreadsheet !== undefined && workbook != null) {
        //load specific workbook
        $("#spreadsheet").igSpreadsheet("option", "workbook", workbook);
    }
}

function upload() {
    var input = document.getElementById('input');
    var file = input.files[0];

    if (file) {
        var formData = new FormData();
        formData.append('file', file);

        // แทน URL ด้านล่างด้วย URL ที่คุณต้องการให้เรียก API การอัปโหลด
        var uploadUrl = 'https://example.com/upload';

        fetch(uploadUrl, {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // ทำสิ่งที่คุณต้องการเมื่ออัปโหลดเสร็จสิ้น
            console.log('Upload success:', data);

            // เรียก setWorkbook() เพื่อให้ Spreadsheet โหลดไฟล์ใหม่
            setWorkbook();
        })
        .catch(error => {
            console.error('Error uploading file:', error);
        });
    } else {
        console.error('No file selected for upload.');
    }
}

function reset() {
    // ล้างข้อมูล Spreadsheet
    $("#spreadsheet").igSpreadsheet("clear");

    // เรียก setWorkbook() เพื่อให้ Spreadsheet เว้นว่าง
    setWorkbook();

}
