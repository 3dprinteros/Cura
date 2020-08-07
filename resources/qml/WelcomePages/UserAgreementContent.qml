// Copyright (c) 2019 Ultimaker B.V.
// Cura is released under the terms of the LGPLv3 or higher.

import QtQuick 2.10
import QtQuick.Controls 2.3

import UM 1.3 as UM
import Cura 1.1 as Cura

//
// This component contains the content for the "User Agreement" page of the welcome on-boarding process.
//
Item
{
    UM.I18nCatalog { id: catalog; name: "cura" }

    Label
    {
        id: titleLabel
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter
        horizontalAlignment: Text.AlignHCenter
        text: catalog.i18nc("@label", "User Agreement")
        color: UM.Theme.getColor("primary_button")
        font: UM.Theme.getFont("huge")
        renderType: Text.NativeRendering
    }

    Label
    {
        id: disclaimerLineLabel
        anchors
        {
            top: titleLabel.bottom
            topMargin: UM.Theme.getSize("wide_margin").height
            left: parent.left
            right: parent.right
        }

        text: "<p> <b> Заявление об отказе от ответственности со стороны DiaPrint </b> </p> "
            + "<p> Пожалуйста, внимательно прочтите этот отказ от ответственности. </p>"
            + "<p> Если иное не указано в письменной форме, DiaPrint предоставляет любое программное обеспечение Imprinta или стороннее программное обеспечение \" как есть \" без каких-либо гарантий. Вы несете весь риск, связанный с качеством и производительностью программного обеспечения DiaPrint. </р>»"
            + "<p> Если это не требуется в соответствии с применимым законодательством или не согласовано в письменной форме, DiaPrint ни при каких обстоятельствах не несет ответственности перед вами за ущерб, включая любые общие, особые, случайные или косвенные убытки, возникшие в результате использования или невозможности использования любого программного обеспечения DiaPrint или стороннего программного обеспечения. </p>"
        textFormat: Text.RichText
        wrapMode: Text.WordWrap
        font: UM.Theme.getFont("medium")
        color: UM.Theme.getColor("text")
        renderType: Text.NativeRendering
    }

    Cura.PrimaryButton
    {
        id: agreeButton
        anchors.right: parent.right
        anchors.bottom: parent.bottom
        text: catalog.i18nc("@button", "Agree")
        onClicked:
        {
            CuraApplication.writeToLog("i", "User accepted the User-Agreement.")
            CuraApplication.setNeedToShowUserAgreement(false)
            base.showNextPage()
        }
    }

    Cura.SecondaryButton
    {
        id: declineButton
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        text: catalog.i18nc("@button", "Decline and close")
        onClicked:
        {
            CuraApplication.writeToLog("i", "User declined the User Agreement.")
            CuraApplication.closeApplication() // NOTE: Hard exit, don't use if anything needs to be saved!
        }
    }
}
