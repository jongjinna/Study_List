package com.jongjinna.website;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class MainController {
  @RequestMapping("/jongjin")
  @ResponseBody
  public String index() {
      return "<h1>Hello! This is jongjin`s website</h1>";
  }
}
