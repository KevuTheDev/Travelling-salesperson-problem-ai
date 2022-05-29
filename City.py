class City:
    def __init__(self, p_name, p_latitude, p_longitude):
        self.m_name = p_name
        self.m_latitude = p_latitude
        self.m_longitude = p_longitude

        return

    def __str__(self):
        return f"{self.m_name:<12} {self.m_latitude:<10} {self.m_longitude:<12}"
        # return "N:" + self.m_name + ", LA:" + str(self.m_latitude) + ", LO:" + str(self.m_longitude)