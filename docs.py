#python printer webportal interaction

#example code from webpage

#every form input proceeds with javascript:
<input value="Go to Next" class="defaultButton" onclick="javascript:adrsWizardForward();" type="button">

#add user form##
<form id="form_STEP" onsubmit="return false;">
<input name="wimToken" value="1949621170" type="hidden">
<input name="stepListIn" class="necessary" value="BASE" id="basic" checked="true" disabled="true" type="checkbox">Basic Information</label>
<label><input name="stepListIn" class="necessary" value="FAX" id="basic" type="checkbox">Fax Destination</label>
<label><input name="stepListIn" class="necessary" value="MAIL" id="basic" type="checkbox">Email Destination</label>
<label><input name="stepListIn" class="necessary" value="FOLDER" id="basic" type="checkbox">Folder Destination</label>
</form>
<input value="Go to Next" class="defaultButton" onclick="javascript:adrsWizardForward();" type="button">

#basic information form##
<form id="form_BASE" onsubmit="return false;">
<input name="wimToken" value="1949621170" type="hidden">
Registration No.(Required):<input name="entryIndexIn" value="00139" class="necessary" size="20" maxlength="5" type="text">
Name(Required):<input name="entryNameIn" value="" class="necessary" size="40" maxlength="20" type="text">
Key Display:<input name="entryDisplayNameIn" value="" size="40" maxlength="16" type="text">
Title 1:<select name="entryTagInfoIn" onchange=""><option value="1" selected="true">None</option><option value="2">AB</option><option value="3">CD</option><option value="4">EF</option><option value="5">GH</option><option value="6">IJK</option><option value="7">LMN</option><option value="8">OPQ</option><option value="9">RST</option><option value="10">UVW</option><option value="11">XYZ</option></select>
Title 2:<select name="entryTagInfoIn" onchange=""><option value="1" selected="true">None</option><option value="2">1</option><option value="3">2</option><option value="4">3</option><option value="5">4</option><option value="6">5</option><option value="7">6</option><option value="8">7</option><option value="9">8</option><option value="10">9</option><option value="11">10</option></select>
Title 3:<select name="entryTagInfoIn" onchange=""><option value="1" selected="true">None</option><option value="2">1</option><option value="3">2</option><option value="4">3</option><option value="5">4</option><option value="6">5</option></select>
Add to Freq.:
<label><input name="entryTagInfoIn" value="1" onclick="" text="On" checked="true" type="radio">On</label>
<label><input name="entryTagInfoIn" value="2" onclick="" text="Off" type="radio">Off</label>
<input value="Go to Next" class="defaultButton" onclick="javascript:adrsWizardForward();" type="button">

#email destination form##
<form id="form_MAIL" onsubmit="return false;">
<input name="wimToken" value="1949621170" type="hidden">
Email Address(Required):<input name="mailAddressIn" value="" class="necessary" size="50" maxlength="128" type="text">
<label><input name="mailSendUserIn" value="true" type="checkbox">Register as both a destination and a sender</label>
</form>
<input value="Go to Next" class="defaultButton" onclick="javascript:adrsWizardForward();" type="button">

#confirm registration form##
<form id="form_CONFIRM" onsubmit="return false;"><input name="wimToken" value="1949621170" type="hidden"></form>
<input value="OK" class="defaultButton" onclick="javascript:adrsWizardForward();" type="button">

#delete user prompt##
<a href="javascript:ConfDelete()" class="commandLabel" onmouseover="changeImage(cmdDelete,'img_DELETE',1)" onmouseout="changeImage(cmdDelete,'img_DELETE',0)">
<nobr><img src="http://10.7.1.63/images/cmdDelete.gif" name="img_DELETE" alt="" title="" border="0" align="absmiddle">Delete</nobr>
</a>

#confirm user deletion##
<a href="javascript:Delete()" class="defaultTableCommandButton">Yes</a>
