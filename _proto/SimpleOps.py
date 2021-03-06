
from ArcCamLib.ArcDSPCommands import ARC_command_list
import fcntl

''' SimpleOps.py '''

__author__     = "Dyer Lytle"
__version__    = "1.0"
__lastupdate__ = "March 15, 2018"

class SimpleOps(object):
    '''
    Simple Camera Operations
    '''
    
    def __init__(self, parent, params):
        '''
        Constructor
        '''
        self.parent = parent
        

    def power_off(self):
        # Send the power on command to the device
        po = ARC_command_list["power_off"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("power_off: Camera not Open", "error")
        else:
            #p = self.parent
            self.parent.writeToConsole("device"
                                       " is doing a 'power_off' command.",
                                       "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                po["board_num"],
                po["command"],
                po["command_type"])
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def power_on(self):
        # Send the power on command to the device
        po = ARC_command_list["power_on"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("power_on: Camera not Open", "error")
        else:
            self.parent.writeToConsole(self.parent.name +
                                       " is doing a 'power_on' command.",
                                       "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                po["board_num"],
                po["command"],
                po["command_type"])
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def start_idle(self):
        # Send the start idle command to the device
        si = ARC_command_list["start_idle"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("start_idle: Camera not Open", "error")
        else:
            self.parent.writeToConsole(self.parent.name +
                                       " is doing a 'start_idle' command.",
                                       "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                si["board_num"],
                si["command"],
                si["command_type"])
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def stop_idle(self):
        # Send the stop idle command to the device
        si = ARC_command_list["stop_idle"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("stop_idle: Camera not Open", "error")
        else:
            self.parent.writeToConsole(self.parent.name +
                                       " is doing a 'stop_idle' command.",
                                       "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                si["board_num"],
                si["command"],
                si["command_type"])
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def set_row_col(self, row, col):
        # Send the row/column command to the device
        src = ARC_command_list["set_row_col"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("set_row_col: Camera not Open", "error")
        else:
            self.parent.writeToConsole(self.parent.name +
                                       " is doing a 'set_row_col' command.",
                                       "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                src["board_num"],
                src["command"],
                src["command_type"],
                row,
                col)
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def set_subframe_size(self, nbias, colsize, rowsize):
        # Send the set subframe size command to the device
        sss = ARC_command_list["set_subframe_size"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "set_subframe_size: Camera not Open", "error")
        else:
            self.parent.writeToConsole(
                self.parent.name + " is doing a 'set_subframe_size' command.",
                "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                sss["board_num"],
                sss["command"],
                sss["command_type"],
                nbias,
                colsize,
                rowsize)
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def set_subframe_position(self, y, x):
        # Send the set subframe position command to the device
        ssp = ARC_command_list["set_subframe_position"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "set_subframe_position: Camera not Open", "error")
        else:
            self.parent.writeToConsole(
                self.parent.name +
                " is doing a 'set_subframe_position' command.", "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                ssp["board_num"],
                ssp["command"],
                ssp["command_type"],
                y,
                x)
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def set_image_parameters(self, frame_type, iframes, srows, interval):
        # Send the set image parameters command to the device
        sip = ARC_command_list["set_image_parameters"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "set_image_parameters: Camera not Open", "error")
        else:
            self.parent.writeToConsole(
                self.parent.name +
                " is doing a 'set_image_parameters' command.", "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                sip["board_num"],
                sip["command"],
                sip["command_type"],
                frame_type,
                iframes,
                srows,
                interval)
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def set_exposure_time(self, exp_time):
        # Send the set exposure time command to the device
        sete = ARC_command_list["set_exposure_time"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "set_exposure_time: Camera not Open", "error")
        else:
            self.parent.writeToConsole(
                self.parent.name +
                " is doing a 'set_exposure_time' command.", "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                sete["board_num"],
                sete["command"],
                sete["command_type"],
                exp_time)
            self.parent.camera_exposure_time = exp_time
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def start_exposure(self):
        # Send the start exposure command to the device
        sex = ARC_command_list["start_exposure"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "start_exposure: Camera not Open", "error")
        else:
            self.parent.writeToConsole(
                self.parent.name +
                " is doing a 'start_exposure' command.", "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                sex["board_num"],
                sex["command"],
                sex["command_type"])
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def clear_subframe(self):
        # Send the clear sub-frame command to the device
        csb = ARC_command_list["clear_subframe"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "clear_subframe: Camera not Open", "error")
        else:
            self.parent.writeToConsole(
                self.parent.name +
                " is doing a 'clear_subframe' command.", "arccam")
            rsp = self.parent.utilities.ioctlCommand(
                csb["board_num"],
                csb["command"],
                csb["command_type"])
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def set_amplifier(self, amp):
        # Send the stop idle command to the device
        sa = ARC_command_list["set_amplifier"]
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "set_amplifier: Camera not Open", "error")
        else:
            self.parent.writeToConsole(self.parent.name +
                                       " is doing a 'set_amplifier' command.",
                                       "arccam")
            
            if (amp not in ['LEFT', 'RIGHT', 'LEFTRIGHT', 'ALL']):
                self.parent.writeToConsole(
                    "Unknown amplifier  in set_amplifier!", "error")
                return('ERR')
            
            output_types = {'LEFT':      0x005F5F4C,
                            'RIGHT':     0x005F5F52,
                            'LEFTRIGHT': 0x005F4C52,
                            'ALL':       0x00414C4C,}
            dsp_amp = output_types[amp]     # Get the hex code for the amp.
            
            # Send the set amplifier command to the device.
            rsp = self.parent.utilities.ioctlCommand(
                sa["board_num"],
                sa["command"],
                sa["command_type"],
                dsp_amp)
            self.parent.utilities.print_text_response(rsp)
        return()
    
    def read_memory(self, board_num, mem_type, dspaddr):
        # Send the read memory command to the device
        rm = ARC_command_list["read_memory"]
        
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("read_memory: Camera not Open", "error")
            return(-1)
        else:
            self.parent.writeToConsole(self.parent.name +
                                       " is doing a 'read_memory' command.",
                                       "arccam")
            
            if (mem_type not in ['R', 'X', 'Y', 'P']):
                self.parent.writeToConsole(
                    "Unknown memory type in read_memory!", "error")
                return('ERR')
            
            mem_types = {'P': 0x100000,
                         'X': 0x200000,
                         'Y': 0x400000,
                         'R': 0x800000,}
            dsp_mem_type = mem_types[mem_type]  # Look up hex for memory type.
            
            # Send the read memory command off to the device.
            rsp = self.parent.utilities.ioctlCommand(
                board_num,
                rm["command"],
                rm["command_type"],
                (dsp_mem_type | dspaddr))
            
            self.parent.utilities.print_hex_response(rsp)  # print memory vals.
            return((rsp[0:3])[::-1])                       # return memory vals.
    
    def write_memory(self, board_num, mem_type, dspaddr, data):
        # Send the write memory command to the device
        wm = ARC_command_list["write_memory"]   # Lookup command in dictionary.
        
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("write_memory: Camera not Open", "error")
        else:
#             self.parent.writeToConsole(self.parent.name +
#                                        " is doing a 'write_memory' command.",
#                                        "arccam")
            
            if (mem_type not in ['R', 'X', 'Y', 'P']):
                self.parent.writeToConsole(
                    "Unknown memory type in read_memory!", "error")
                return('ERR')   # Bad memory type.
            
            mem_types = {'P': 0x100000,
                         'X': 0x200000,
                         'Y': 0x400000,
                         'R': 0x800000,}
            dsp_mem_type = mem_types[mem_type]   # Get hex code for memory type.
            
            # Sent the write memory command off to the device.
            rsp = self.parent.utilities.ioctlCommand(
                board_num,
                wm["command"],
                wm["command_type"],
                (dsp_mem_type | dspaddr),
                data)
            
            #self.parent.utilities.print_hex_response(rsp)
        return()
    
    def status(self):
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole("check_status: Camera not Open", "error")
            return("Status Unknown, Camera not Open")
        mycmdint = 0
        mycmd = mycmdint.to_bytes(4, byteorder='little')
        result = fcntl.ioctl(self.parent.camera_file_descriptor, 0x4, mycmd)

        rval = int.from_bytes(result, byteorder='little')
        if (rval == 3):
            self.parent.writeToConsole("status: Camera ready", "arccam")
            return("getHSTR returns 3, camera/controller ready")
        else:
            self.parent.writeToConsole("status: Camera not ready", "error")
            return ("getHSTR did not return 3, there is a problem")
        
    def reset_controller(self):
        if (not self.parent.file_descriptor_open):
            self.parent.writeToConsole(
                "reset_controller: Camera not Open", "error")
            return("Cannot reset controller, Camera not Open")
        
        mycmdint = 0x8077   # PCI_PC_RESET
        mycmd = mycmdint.to_bytes(4, byteorder='little')
        rsp = fcntl.ioctl(self.parent.camera_file_descriptor, 0x12, mycmd)
        self.parent.utilities.print_hex_response(rsp)

        mycmdint = 0x87     # RESET_CONTROLLER
        mycmd = mycmdint.to_bytes(4, byteorder='little')
        rsp = fcntl.ioctl(self.parent.camera_file_descriptor, 0x12, mycmd)
        self.parent.utilities.print_hex_response(rsp)
        
    
