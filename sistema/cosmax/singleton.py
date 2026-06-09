class ConfiguracionSistema:
    STOCK_BAJO = 5
    IVA = 0.21
    NOMBRE_SISTEMA = "COSMAX"
    SIN_STOCK = 0

    def __new__(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ConfiguracionSistema, cls).__new__(cls)
        return cls._instance