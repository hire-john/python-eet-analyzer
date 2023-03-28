class Units:

    def metric(self, metric):
        result = 0
        match metric:
            case "deka":
                result = pow(10, 1)
            case "hecto":
                result = pow(10, 2)
            case "kilo":
                result = pow(10, 3)
            case "mega":
                result = pow(10, 6)
            case "giga":
                result = pow(10, 9)
            case "tera":
                result = pow(10, 12)
            case "peta":
                result = pow(10, 15)
            case "exa":
                result = pow(10, 18)
            case "zetta":
                result = pow(10, 21)
            case "yotta":
                result = pow(10, 24)
            case "ronna":
                result = pow(10, 27)
            case "quetta":
                result = pow(10, 30)
        return result
