# Initialize lists
parameter_names = []
parameter_values = []
input_names = []
input_widths = []
output_names = []
output_widths = []
output_types = []


# List of special characters

special_characters = set("!@#$%^&*()+=[]{}|\\;:'\",<>/?~`-.")
reserved_v = [
        "always", "and", "assign", "automatic", "begin", "buf", "bufif0", "bufif1", "case",
        "casex", "casez", "cell", "cmos", "config", "deassign", "default", "defparam", "design",
        "disable", "edge", "else", "end", "endcase", "endconfig", "endfunction", "endgenerate",
        "endmodule", "endprimitive", "endspecify", "endtable", "endtask", "event", "for",
        "force", "forever", "fork", "function", "generate", "genvar", "highz0", "highz1",
        "if", "ifdef", "ifndef", "initial", "inout", "input", "instance", "integer", "join",
        "large", "liblist", "library", "localparam", "macromodule", "medium", "module", "nand",
        "negedge", "nmos", "nor", "noshowcancelled", "not", "notif0", "notif1", "or",
        "output", "parameter", "pmos", "posedge", "primitive", "pull0", "pull1", "pulldown",
        "pullup", "pulsestyle_onevent", "pulsestyle_ondetect", "rcmos", "real", "realtime",
        "reg", "release", "repeat", "rnmos", "rpmos", "rtran", "rtranif0", "rtranif1",
        "scalared", "showcancelled", "signed", "small", "specify", "specparam", "strong0",
        "strong1", "supply0", "supply1", "table", "task", "time", "tran", "tranif0",
        "tranif1", "tri", "tri0", "tri1", "triand", "trior", "trireg", "unsigned", "use",
        "vectored", "wait", "wand", "weak0", "weak1", "while", "wire", "wor", "xnor", "xor"
    ]

print("Welcome to my script\n")

# Enter the module name 

while True:
    module_name = input("What is your module name: ")
    if  module_name[0] not in special_characters and not module_name[0].isdigit() and module_name not in reserved_v:
        break
    else:
        print("Invalid Module Name. Please enter a valid name.")
        

# Enter the number of inputs and outputs

while True:
    num_inputs = input("How many inputs do you have? ")
    if  num_inputs.isdigit():
        break
    else:
        print("Invalid number. Please enter a valid integer.")
        
while True:
    num_outputs = input("How many outputs do you have? ")
    if  num_outputs.isdigit():
        break
    else:
        print("Invalid number. Please enter a valid integer.")


# Enter parameters names and values

while True:
    parameters_num = input("How many parameters do you have? ")
    if parameters_num.isdigit():
        break
    else:
        print("Invalid parameter number. Please enter an integer value.")


if int(parameters_num) == 0:
    print("YOU DON'T HAVE ANY PARAMETERS")
else:
    for i in range(int(parameters_num)):
        while True:
            name = input(f"Please enter unique parameter name {i+1}: ")
            if name not in parameter_names and name.isalpha():
                parameter_names.append(name)
                break
            else:
                print("Parameter name already exists or Invalid. Please enter a unique name.")
                
                
        while True:
            value = input(f"Please enter parameter value {i+1}: ")
            if value.isdigit():
                parameter_values.append(int(value))
                break
            else:
                print("Invalid parameter value. Please enter an integer value.")
                
                
                
# Enter the inputs names and widths and define if it's parameterized or not

for i in range(int(num_inputs)):
    while True:
        name = input(f"Enter unique input name {i+1}: ")
        if name not in input_names and (name.isalpha() or name[0] == "_"):
            input_names.append(name)
            
            if int(parameters_num) != 0:
                while True:
                    ans1 = input("Is the input parametrized? (Y/y/1) for yes and (N/n/0) for no: ")
                    if ans1 in {"1", "Y", "y"}:
                        print("Parameters Names --> ", parameter_names)
                        while True:
                            choose2 = input("Write Name of Parameter for input: ")
                            if choose2 in parameter_names and choose2.isalpha():
                                input_widths.append(choose2)
                                break
                            else:
                                print("Invalid parameter name. Please enter a valid parameter name from the list.")
                        break
                    elif ans1 in {"0", "N", "n"}:
                        while True:
                            width = input(f"Enter the input width {i+1}: ")
                            if width.isdigit():
                                input_widths.append(int(width))
                                break
                            else:
                                print("Invalid input width. Please enter an integer value.")
                        break
                    else:
                        print("Invalid input. Please enter (Y/y/1) for yes or (N/n/0) for no.")
            else:
                while True:
                    width = input(f"Enter the input width {i+1}: ")
                    if width.isdigit():
                        input_widths.append(int(width))
                        break
                    else:
                        print("Invalid input width. Please enter an integer value.")
            break
        else:
            print("Input name already exists or Invalid name. Please enter a unique name.")


   

# Enter the outputs names and widths and define if it's parameterized or not or reg or wire

for i in range(int(num_outputs)):
    while True:
        name = input(f"Enter unique output name {i+1}: ")
        if name not in output_names and name not in parameter_names and name not in input_names and (name.isalpha() or name[0] == "_"):
            output_names.append(name)
            
            while True:
                Type = input(f"Is output {name} a reg or wire? (reg/wire): ")
                if Type in {"reg", "wire"}:
                    output_types.append(Type)
                    break
                else:
                    print("Invalid type. Please enter 'reg' or 'wire'.")
            
            if int(parameters_num) != 0:     
                while True:
                    ans2 = input("Are the outputs parametrized? (Y/y/1 for yes, N/n/0 for no): ")
                    if ans2 in {"1", "Y", "y"}:
                        print("Parameters Names --> ", parameter_names)
                        while True:
                            choose2 = input("Write Name of Parameter: ")
                            if choose2 in parameter_names and choose2.isalpha():
                                output_widths.append(choose2)
                                break
                            else:
                                print("Invalid parameter name. Please enter a valid parameter name from the list.")
                        break
                    elif ans2 in {"0", "N", "n"}:
                        while True:
                            width = input(f"Enter the output width {i+1}: ")
                            if width.isdigit():
                                output_widths.append(int(width))
                                break
                            else:
                                print("Invalid output width. Please enter an integer value.")
                        break
                    else:
                        print("Invalid input. Please enter (Y/y/1) for yes or (N/n/0) for no.")
            else:
                while True:
                    width = input(f"Enter the output width {i+1}: ")
                    if width.isdigit():
                        output_widths.append(int(width))
                        break
                    else:
                        print("Invalid output width. Please enter an integer value.")
            break
        else:
            print("Output name already exists or Invalid name. Please enter a unique name.")
            
            

# Enter the circuit type

while True:
    circuit_type = input("Is the circuit seq or comb? (seq/comb): ")
    if circuit_type in {"seq", "comb"}:
        break
    else:
        print("Invalid type. Please enter 'seq' for seq or 'comb' for comb.")

# If the circuit is sequential, ask for clock and reset details

if circuit_type == "seq":
    clk_name = input("Enter the clock name: ")
    
    while True:
        clk_type = (input("Is posedge sens or negedge sens? (1 for pos / 0 for neg): "))
        if int(clk_type) in {1,0}:
            break
        else:
            print("Invalid type. Please enter '1' for synch or '0' for asynch.")
    
    reset_needed = input("Is there a reset? (Y/y/1) for yes and (N/n/0) for no: ")
    if reset_needed in {"1", "Y", "y"}:
        reset_name = input("Enter the reset signal: ")
        
        while True:
            reset_type = (input("Is the reset synchronous or asynchronous? (1 for synch / 0 for asynch): "))
            if int(reset_type) in {1,0}:
                break
            else:
                print("Invalid type. Please enter '1' for synch or '0' for asynch.")
        
        while True:
            reset_active = (input("Is the reset active low or active high? (0 for low / 1 for high): "))
            if int(reset_active) in {1,0}:
                break
            else:
                print("Invalid type. Please enter '0' for active low or '1' for active high.")
                
                
        ####################################Code for seq circuit with reset######################################
        
        def write_verilog(module_name, parameter_names,parameter_values,input_names,input_widths,output_names,output_widths,
                      output_types,clk_name,clk_type,reset_name,reset_type,reset_active):
        
            with open(f"{module_name}.v", "w") as file:
                
                # Module declaration
                file.write(f"module {module_name} (\n")
                
                # Ports declaration
                file.write(f"     {clk_name},\n")
                file.write(f"     {reset_name},\n")
                for inputs in input_names:
                    width = input_widths[input_names.index(inputs)]
                    if isinstance(width, str):
                        file.write(f"     {inputs},\n")
                    else:
                        file.write(f"     {inputs},\n")
                        
                for outputs in output_names:
                    width = output_widths[output_names.index(outputs)]
                    if isinstance(width, str):
                        for outputs in output_names:
                            if (len (outputs) == 1):
                                file.write(f"     {outputs}\n")
                            else: 
                                if (outputs.index(outputs) == len (outputs) - 1):
                                    file.write(f"     {outputs}\n")
                                else:
                                    file.write(f"     {outputs},\n")
                    else:
                        if (len (outputs) == 1):
                            file.write(f"     {outputs}\n")
                        else: 
                            if (outputs.index(outputs) == len (outputs) - 1):
                                file.write(f"     {outputs}\n")
                            else:
                                file.write(f"     {outputs},\n")


                file.write(");\n\n")
                
                # Parameters declaration
                for param, value in zip(parameter_names, parameter_values):
                    file.write(f"parameter {param} = {value};\n")
                
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"         \n")
                
                
                file.write(f"input wire {clk_name};\n")
                file.write(f"input wire {reset_name};\n")
                           
                # Inputs definition
                for name, width in zip(input_names, input_widths):
                    if isinstance(width, str):
                        file.write(f"input wire [{width}-1:0] {name};\n")
                    else:
                        file.write(f"input wire [{width-1}:0] {name};\n")
                
                # Outputs definition
                for name, width, ttype in zip(output_names, output_widths, output_types):
                    if isinstance(width, str):
                        file.write(f"output {ttype} [{width}-1:0] {name};\n")
                    else:
                        file.write(f"output {ttype} [{width-1}:0] {name};\n")
                        
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"         \n")

                # Module Body
                if int(clk_type) == 0 and int(reset_type) == 0 and int(reset_active) == 0: 
                    file.write(f"always @ (posedge {clk_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if ({reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                 
                elif int(clk_type) == 0 and int(reset_type) == 0 and int(reset_active) == 1:   
                    file.write(f"always @ (negedge {clk_name} or posedge {reset_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if ({reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                
                elif int(clk_type) == 0 and int(reset_type) == 1 and int(reset_active) == 0:   
                    file.write(f"always @ (negedge {clk_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if (!{reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                
                elif int(clk_type) == 0 and int(reset_type) == 1 and int(reset_active) == 1:   
                    file.write(f"always @ (negedge {clk_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if ({reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                
                
                elif int(clk_type) == 1 and int(reset_type) == 0 and int(reset_active) == 0:   
                    file.write(f"always @ (posedge {clk_name} or negedge {reset_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if (!{reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                
                elif int(clk_type) == 1 and int(reset_type) == 0 and int(reset_active) == 1:   
                    file.write(f"always @ (posedge {clk_name} or posedge {reset_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if ({reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                
                elif int(clk_type) == 1 and int(reset_type) == 1 and int(reset_active) == 0:   
                    file.write(f"always @ (posedge {clk_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if (!{reset_name}) \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
            
                
                elif int(clk_type) == 1 and int(reset_type) == 1 and int(reset_active) == 1:   
                    file.write(f"always @ (posedge {clk_name})\n")
                    file.write(f"begin \n")
                    file.write(f"    if ({reset_name}) (\n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"    else  \n")
                    file.write(f"       begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"       end  \n")
                    file.write(f"end  \n")
                
                file.write("\nendmodule")
                
            
#####################################TB Generating for a seq circuit with reset######################################
                
                with open(f"{module_name}_TB.v", "w") as file:
                    
                    # TB Module declaration
                    file.write(f"module {module_name}_TB(); \n")
                    
                    # TB signals decleration
                    
                    for param, value in zip(parameter_names, parameter_values):
                        file.write(f"  parameter {param} = {value};\n")
                    
                    file.write(f"  parameter clk_period = your_period;  // change(your_period)with the actual value of your period)\n")
                    file.write(f"  reg   {clk_name}_TB;\n")
                    file.write(f"  reg   {reset_name}_TB;\n")
                    
                    
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    
                    for name, width in zip(input_names, input_widths):
                        if isinstance(width, str):
                            file.write(f"reg [{width}-1:0] {name}_TB;\n")
                        else:
                            file.write(f"reg [{width-1}:0] {name}_TB;\n")
                    
                    # Outputs definition
                    for name, width in zip(output_names, output_widths):
                        if isinstance(width, str):
                            file.write(f"wire [{width}-1:0] {name}_TB;\n")
                        else:
                            file.write(f"wire [{width-1}:0] {name}_TB;\n")
                            
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")

                    # instantiation
                     
                    file.write(f"{module_name}  DUT\n")
                    file.write(f"( \n")
                    file.write(f"     .{clk_name} ({clk_name}_TB),\n")
                    file.write(f"     .{reset_name} ({reset_name}_TB),\n")
                    
                    for inputs in input_names:
                            file.write(f"     .{inputs} ({inputs}_TB),\n")
                            
                    for outputs in output_names:
                        if (len (outputs) == 1):
                            file.write(f"     .{outputs} ({outputs}_TB)\n")
                        else: 
                            if (outputs.index(outputs) == len (outputs) - 1):
                                file.write(f"     .{outputs} ({outputs}_TB)\n")
                            else:
                                file.write(f"     .{outputs} ({outputs}_TB),\n")
                            
                    file.write(");\n\n")
                        
                    file.write(f"    //clock_generator       \n")
                    file.write(f"    always #clk_period  {clk_name}_TB = ~{clk_name}_TB;    \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    
                    file.write(f"initial \n")
                    file.write(f"begin \n")
                    file.write(f"    //initialize the clk and TB signals here \n")
                    file.write(f"    {clk_name}_TB = 1'b0;   \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"    //write your 1st test case here        \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"    //write your 2nd test case here        \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"end  \n")
                    
                    file.write("\nendmodule")
                
                
        write_verilog(module_name, parameter_names,parameter_values,input_names,input_widths,output_names,output_widths,
                      output_types,clk_name,clk_type,reset_name,reset_type,reset_active)
                      
    
    
    else: ####################################Code for seq circuit without reset###########################
        
        def write_verilog(module_name, parameter_names,parameter_values,input_names,input_widths,output_names,output_widths,
                      output_types,clk_name,clk_type):
        
            with open(f"{module_name}.v", "w") as file:
                
                # Module declaration
                file.write(f"module {module_name} (\n")
                
                # Ports declaration
                file.write(f"     {clk_name},\n")
                for inputs in input_names:
                    width = input_widths[input_names.index(inputs)]
                    if isinstance(width, str):
                        file.write(f"     {inputs},\n")
                    else:
                        file.write(f"     {inputs},\n")
                        
                for outputs in output_names:
                    width = output_widths[output_names.index(outputs)]
                    if isinstance(width, str):
                        for outputs in output_names:
                            if (len (outputs) == 1):
                                file.write(f"     {outputs}\n")
                            else: 
                                if (outputs.index(outputs) == len (outputs) - 1):
                                    file.write(f"     {outputs}\n")
                                else:
                                    file.write(f"     {outputs},\n")
                    else:
                        if (len (outputs) == 1):
                            file.write(f"     {outputs}\n")
                        else: 
                            if (outputs.index(outputs) == len (outputs) - 1):
                                file.write(f"     {outputs}\n")
                            else:
                                file.write(f"     {outputs},\n")
                            
                file.write(");\n\n")
                
                # Parameters declaration
                for param, value in zip(parameter_names, parameter_values):
                    file.write(f"parameter {param} = {value};\n")
                
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"         \n")
                
                
                file.write(f"input wire {clk_name};\n")
                file.write(f"input wire {reset_name};\n")
                
                # Inputs definition
                for name, width in zip(input_names, input_widths):
                    if isinstance(width, str):
                        file.write(f"input wire [{width}-1:0] {name};\n")
                    else:
                        file.write(f"input wire [{width-1}:0] {name};\n")
                
                # Outputs definition
                for name, width, ttype in zip(output_names, output_widths, output_types):
                    if isinstance(width, str):
                        file.write(f"output {ttype} [{width}-1:0] {name};\n")
                    else:
                        file.write(f"output {ttype} [{width-1}:0] {name};\n")
                        
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"         \n")
                    
                
                # Module Body
                if clk_type == 0:
                     file.write(f"always @ (negedge {clk_name})\n")
                     file.write(f"begin  \n")
                     file.write(f"         \n")
                     file.write(f"         \n")
                     file.write(f"         \n")
                     file.write(f"end  \n")                 
                 
                else:
                    file.write(f"always @ (posedge {clk_name})\n")
                    file.write(f"begin  \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"end  \n")
                
                file.write("\nendmodule")

                
###################################TB Generating for a seq circuit without reset#####################################
                
                with open(f"{module_name}_TB.v", "w") as file:
                    
                    # TB Module declaration
                    file.write(f"module {module_name}_TB(); \n")
                    
                    # TB signals decleration
                    
                    for param, value in zip(parameter_names, parameter_values):
                        file.write(f"  parameter {param} = {value};\n")
                    
                    file.write(f"  parameter clk_period = your_period;  // change(your_period)with the actual value of your period)\n")
                    file.write(f"  reg   {clk_name}_TB;\n")
                    
                    
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    
                    for name, width in zip(input_names, input_widths):
                        if isinstance(width, str):
                            file.write(f"reg [{width}-1:0] {name}_TB;\n")
                        else:
                            file.write(f"reg [{width-1}:0] {name}_TB;\n")
                    
                    # Outputs definition
                    for name, width in zip(output_names, output_widths):
                        if isinstance(width, str):
                            file.write(f"wire [{width}-1:0] {name}_TB;\n")
                        else:
                            file.write(f"wire [{width-1}:0] {name}_TB;\n")
                            
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"         \n")

                    # instantiation
                     
                    file.write(f"{module_name}  DUT\n")
                    file.write(f"( \n")
                    file.write(f"     .{clk_name} ({clk_name}_TB),\n")
                    
                    for inputs in input_names:
                            file.write(f"     .{inputs} ({inputs}_TB),\n")
                            
                    for outputs in output_names:
                        if (len (outputs) == 1):
                            file.write(f"     .{outputs} ({outputs}_TB)\n")
                        else: 
                            if (outputs.index(outputs) == len (outputs) - 1):
                                file.write(f"     .{outputs} ({outputs}_TB)\n")
                            else:
                                file.write(f"     .{outputs} ({outputs}_TB),\n")
                            
                    file.write(");\n\n")
                    
                    file.write(f"    //clock_generator       \n")
                    file.write(f"    always #clk_period  {clk_name}_TB = ~{clk_name}_TB;    \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    
                    file.write(f"initial \n")
                    file.write(f"begin \n")
                    file.write(f"    //initialize the clk and TB signals here \n")
                    file.write(f"    {clk_name}_TB = 1'b0;   \n")
                    file.write(f"         \n")
                    file.write(f"    //write your 1st test case here        \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"    //write your 2nd test case here        \n")
                    file.write(f"         \n")
                    file.write(f"         \n")
                    file.write(f"end  \n")
                    
                    file.write("\nendmodule")				
                
        write_verilog(module_name, parameter_names,parameter_values,input_names,input_widths,output_names,output_widths,
                      output_types,clk_name,clk_type)
 
else: #############################################Code for comb circuit#########################################
    
    def write_verilog_comb(module_name,parameter_names,parameter_values,input_names,input_widths,output_names,
                          output_widths,output_types
                          ):
        
        with open(f"{module_name}.v", "w") as file:
            
            # Module declaration
            file.write(f"module {module_name} (\n")
            
            # Ports declaration
            for inputs in input_names:
                width = input_widths[input_names.index(inputs)]
                if isinstance(width, str):
                    file.write(f"    {inputs},\n")
                else:
                    file.write(f"    {inputs},\n")
                    
            for outputs in output_names:
                width = output_widths[output_names.index(outputs)]
                if isinstance(width, str):
                    for outputs in output_names:
                        if (len (outputs) == 1):
                            file.write(f"     {outputs}\n")
                        else: 
                            if (outputs.index(outputs) == len (outputs) - 1):
                                file.write(f"     {outputs}\n")
                            else:
                                file.write(f"     {outputs},\n")
                else:
                    if (len (outputs) == 1):
                        file.write(f"     {outputs}\n")
                    else: 
                        if (outputs.index(outputs) == len (outputs) - 1):
                            file.write(f"     {outputs}\n")
                        else:
                            file.write(f"     {outputs},\n")
                        
            file.write(");\n\n")
            
            # Parameters declaration
            for param, value in zip(parameter_names, parameter_values):
                file.write(f"parameter {param} = {value};\n")
            
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"         \n")
            
            # Inputs definition
            for name, width in zip(input_names, input_widths):
                if isinstance(width, str):
                    file.write(f"input wire [{width}-1:0] {name};\n")
                else:
                    file.write(f"input wire [{width-1}:0] {name};\n")
            
            # Outputs definition
            for name, width, ttype in zip(output_names, output_widths, output_types):
                if isinstance(width, str):
                    file.write(f"output {ttype} [{width}-1:0] {name};\n")
                else:
                    file.write(f"output {ttype} [{width-1}:0] {name};\n")
                    
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"         \n")
            
            # Module Body
            file.write(f"always @ (*)\n")
            file.write(f"begin \n")
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"         \n")
            file.write(f"end  \n")
                
            file.write("\nendmodule")
            
            
######################################TB Generating for a comb circuit###############################################
                
            with open(f"{module_name}_TB.v", "w") as file:
                    
                # TB Module declaration
                file.write(f"module {module_name}_TB(); \n")
                    
                # TB signals decleration
                    
                for param, value in zip(parameter_names, parameter_values):
                    file.write(f"  parameter {param} = {value};\n")
                    
                    
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"         \n")
                    
                for name, width in zip(input_names, input_widths):
                    if isinstance(width, str):
                        file.write(f"reg [{width}-1:0] {name}_TB;\n")
                    else:
                        file.write(f"reg [{width-1}:0] {name}_TB;\n")
                    
                # Outputs definition
                for name, width in zip(output_names, output_widths):
                    if isinstance(width, str):
                        file.write(f"wire [{width}-1:0] {name}_TB;\n")
                    else:
                        file.write(f"wire [{width-1}:0] {name}_TB;\n")
                            
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"         \n")

                # instantiation
                     
                file.write(f"{module_name}  DUT\n")
                file.write(f"( \n")
                    
                for inputs in input_names:
                    file.write(f"     .{inputs} ({inputs}_TB),\n")
                            
                for outputs in output_names:
                    if (len (outputs) == 1):
                        file.write(f"     .{outputs} ({outputs}_TB)\n")
                    else: 
                        if (outputs.index(outputs) == len (outputs) - 1):
                            file.write(f"     .{outputs} ({outputs}_TB)\n")
                        else:
                            file.write(f"     .{outputs} ({outputs}_TB),\n")
                            
                file.write(");\n\n")
                        
                file.write(f"initial \n")
                file.write(f"begin \n")
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"    //write your 1st test case here        \n")
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"    //write your 2nd test case here        \n")
                file.write(f"         \n")
                file.write(f"         \n")
                file.write(f"end  \n")
                
                file.write("\nendmodule")

    write_verilog_comb(module_name, parameter_names, parameter_values, input_names, input_widths, output_names,
                       output_widths,output_types)



print(f"\nVerilog file '{module_name}.v' has been generated successfully!")
print(f"\nVerilog file '{module_name}_TB.v' has been generated successfully!")
