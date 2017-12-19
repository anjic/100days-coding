import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ServerWwnFormComponent } from './server-wwn-form.component';

describe('ServerWwnFormComponent', () => {
  let component: ServerWwnFormComponent;
  let fixture: ComponentFixture<ServerWwnFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ServerWwnFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ServerWwnFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
