module carryadd_tb;
    reg [3:0] A, B;
    reg Cin;
    wire [3:0] Sum;
    wire Cout;
    
    carryadd uut(.A(A), .B(B), .Cin(Cin), .Sum(Sum), .Cout(Cout));

    integer infile, outfile, temp;
    reg [8:0] vector;

    initial begin
    
        $dumpfile("carryadd.vcd");
        $dumpvars(0, carryadd_tb);

        
        infile = $fopen("input_vectors.txt", "r");
        if (infile == 0) begin
            $display("Input file not found");
            $finish;
        end

        
        outfile = $fopen("orangeoutput.txt", "w");
        if (outfile == 0) begin
            $display("Failed to open output results file");
            $finish;
        end

        
        while (!$feof(infile)) begin
            temp = $fscanf(infile, "%b", vector);

            
            A = vector[8:5];   
            B = vector[4:1];  
            Cin = vector[0];  

            #10; 
            
            $display("A=%b B=%b Cin=%b Sum=%b Cout=%b", A, B, Cin, Sum, Cout);

            $fwrite(outfile, "%b%b\n", Sum, Cout);
        end

        $fclose(infile);
        $fclose(outfile);

        $finish;
    end
endmodule

