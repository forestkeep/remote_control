



class device:
    """device parameters"""

    def __init__(self,model,type_of_connection,protocol) -> None:
        self.model = model
        self.type_of_connection = type_of_connection
        self.protocol = protocol
    def get_model(self):
        return self.model
        
     
class powersupply(device):
	def __init__(self,model,type_of_connection,protocol,number_of_channel):
		super().__init__(model,type_of_connection,protocol)
		self.number_of_channel = number_of_channel


        
